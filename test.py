import cv2
import numpy as np
import sqlite3
import os

class FaceMatchingSystem:
    def __init__(self, database_path='face_database.db'):
        """
        Initialize the face matching system with a SQLite database
        
        Args:
            database_path (str): Path to the SQLite database file
        """
        # Ensure directory exists
        os.makedirs(os.path.dirname(database_path) or '.', exist_ok=True)
        
        # Database connection
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()
        
        # Create table for storing face features
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS face_features (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT UNIQUE,
                feature_vector BLOB,
                name TEXT
            )
        ''')
        self.conn.commit()

        # Initialize feature extractor and matcher
        self.feature_extractor = cv2.ORB_create()
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    def extract_features(self, image_path):
        """
        Extract features from an image
        
        Args:
            image_path (str): Path to the image file
        
        Returns:
            tuple: Keypoints and descriptors
        """
        # Read image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if image is None:
            print(f"Error: Could not read image {image_path}")
            return None, None
        
        # Detect keypoints and compute descriptors
        keypoints, descriptors = self.feature_extractor.detectAndCompute(image, None)
        
        return keypoints, descriptors

    def store_face_features(self, image_path, name=None):
        """
        Store face features in the database
        
        Args:
            image_path (str): Path to the image file
            name (str, optional): Name associated with the face
        
        Returns:
            bool: Success status
        """
        # Extract features
        keypoints, descriptors = self.extract_features(image_path)
        
        if descriptors is None:
            print(f"No features found in {image_path}")
            return False
        
        try:
            # Convert descriptors to binary for storage
            feature_vector = descriptors.tobytes()
            
            # Insert or replace in database
            self.cursor.execute('''
                INSERT OR REPLACE INTO face_features 
                (image_path, feature_vector, name) 
                VALUES (?, ?, ?)
            ''', (image_path, feature_vector, name))
            
            self.conn.commit()
            return True
        
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def compare_faces(self, sketch_path, top_n=5):
        """
        Compare a sketch to all stored face images
        
        Args:
            sketch_path (str): Path to the sketch image
            top_n (int): Number of top matches to return
        
        Returns:
            list: Top matches with similarity percentages
        """
        # Extract features from sketch
        sketch_keypoints, sketch_descriptors = self.extract_features(sketch_path)
        
        if sketch_descriptors is None:
            print("No features found in sketch")
            return []
        
        # Retrieve all stored face features
        self.cursor.execute('SELECT image_path, feature_vector, name FROM face_features')
        matches = []
        
        for db_path, blob_features, name in self.cursor.fetchall():
            # Convert stored blob back to numpy array
            stored_descriptors = np.frombuffer(blob_features, dtype=np.uint8).reshape(-1, 32)
            
            # Match descriptors
            match_results = self.matcher.match(sketch_descriptors, stored_descriptors)
            
            # Calculate similarity based on matches
            if match_results:
                # Sort matches by distance (lower is better)
                match_results = sorted(match_results, key=lambda x: x.distance)
                
                # Calculate similarity percentage
                similarity = max(100 - (sum(m.distance for m in match_results[:10]) / 10), 0)
                
                matches.append({
                    'image_path': db_path,
                    'name': name,
                    'similarity': similarity
                })
        
        # Sort matches by similarity in descending order
        matches.sort(key=lambda x: x['similarity'], reverse=True)
        
        return matches[:top_n]

    def load_images_to_database(self, image_directory):
        """
        Load all images from a directory to the database
        
        Args:
            image_directory (str): Path to directory with real face images
        """
        # Supported image extensions
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        
        # Iterate through images and store features
        for filename in os.listdir(image_directory):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_path = os.path.join(image_directory, filename)
                # Use filename (without extension) as name
                name = os.path.splitext(filename)[0]
                self.store_face_features(image_path, name)
        
        print(f"Loaded face features from {image_directory}")

    def close_connection(self):
        """Close database connection"""
        self.conn.close()

def main():
    # Paths
    real_images_path = r'C:\Users\Radesh\Desktop\open\real_image'
    sketch_path = r'C:\Users\Radesh\Desktop\open\sketches'
    
    image = cv2.imread(sketch_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
       print("Error: Could not read the image file.")
    else:
       print("Image loaded successfully.")
    # Create face matching system
    face_system = FaceMatchingSystem('face_database.db')
    
    # Load real face images to database
    face_system.load_images_to_database(real_images_path)
    
    # Compare a sketch to database
    matches = face_system.compare_faces(sketch_path)
    
    # Print results
    print("Top Matches:")
    for match in matches:
        print(f"Image: {match['image_path']}")
        print(f"Name: {match['name']}")
        print(f"Similarity: {match['similarity']:.2f}%")
        print("---")
    
    # Close database connection
    face_system.close_connection()

if __name__ == "__main__":
    main()
