# Face Sketch Detection Using ORB Algorithm

A web-based face matching system that compares hand-drawn sketches with real face images using the ORB (Oriented FAST and Rotated BRIEF) algorithm. This project provides an intuitive web interface for uploading face images and sketches, then finding the best matches based on feature similarity.

## 🎯 Features

- **Feature Extraction**: Uses ORB algorithm to detect keypoints and compute descriptors
- **Database Storage**: SQLite database for efficient storage and retrieval of face features
- **Web Interface**: Flask-based web application with drag-and-drop file upload
- **Real-time Matching**: Instant comparison and ranking of sketch-to-face matches
- **Similarity Scoring**: Percentage-based similarity scores for each match
- **Multiple Image Support**: Upload multiple real face images for comparison
- **Responsive Design**: Clean, modern UI that works on desktop and mobile

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask
- **Computer Vision**: OpenCV (cv2)
- **Feature Detection**: ORB (Oriented FAST and Rotated BRIEF)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Dependencies**: numpy, opencv-python, flask

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Face_Sketch_Detection_Using_ORB_Algorithm_python.git
   cd Face_Sketch_Detection_Using_ORB_Algorithm_python
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   myenv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source myenv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install flask opencv-python numpy
   ```

## 🎮 Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your web browser**
   Navigate to `http://localhost:5000`

3. **Upload images**
   - Upload multiple real face images (JPG, PNG, BMP)
   - Upload a single sketch image for comparison

4. **View results**
   - The system will automatically process the images
   - View top matches with similarity percentages
   - Clear the database if needed for new comparisons

## 📁 Project Structure

```
Face_Sketch_Detection_Using_ORB_Algorithm_python/
├── app.py                 # Main Flask application
├── test.py               # Core face matching system
├── templates/
│   └── index.html        # Web interface template
├── static/
│   └── uploads/          # Uploaded images storage
│       ├── real_images/  # Real face images
│       └── sketch/       # Sketch images
├── real_image/           # Sample real face images
├── sketches/             # Sample sketch images
├── myenv/                # Virtual environment
└── README.md            # This file
```

## 🔧 How It Works

### 1. Feature Extraction
- Uses ORB algorithm to detect keypoints in both real images and sketches
- Computes binary descriptors for efficient matching
- Handles grayscale image processing for optimal feature detection

### 2. Database Management
- Stores extracted features as binary blobs in SQLite database
- Maintains image paths and associated names
- Enables fast retrieval and comparison of stored features

### 3. Matching Algorithm
- Uses BFMatcher (Brute Force Matcher) with Hamming distance
- Compares sketch descriptors with all stored face descriptors
- Calculates similarity scores based on match distances

### 4. Result Ranking
- Sorts matches by similarity percentage
- Returns top N matches (default: 5)
- Provides visual comparison with similarity scores

## 📊 Algorithm Details

### ORB (Oriented FAST and Rotated BRIEF)
- **FAST**: Detects keypoints using corner detection
- **BRIEF**: Computes binary descriptors for keypoints
- **Oriented**: Adds rotation invariance to features
- **Advantages**: Fast, efficient, and suitable for real-time applications

### Feature Matching
- **BFMatcher**: Brute force matching with Hamming distance
- **Cross-check**: Ensures mutual best matches
- **Distance calculation**: Lower distance = higher similarity
- **Similarity scoring**: Converts distances to percentage scores

## 🎨 Web Interface Features

- **Drag-and-drop file upload**
- **Multiple file selection**
- **Real-time processing**
- **Visual result display**
- **Database management**
- **Responsive design**

## 🔍 Sample Usage

1. Upload several real face images of different people
2. Upload a hand-drawn sketch of one of those people
3. The system will:
   - Extract features from all images
   - Compare the sketch with stored faces
   - Display top matches with similarity scores
   - Show visual comparison of results

## 🐛 Troubleshooting

### Common Issues

1. **Import Error**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Error**: Clear the database using the "Clear Database" button

3. **Image Loading Error**: Ensure images are in supported formats (JPG, PNG, BMP)

4. **Port Already in Use**: Change the port in `app.py`
   ```python
   app.run(debug=True, port=5001)
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- Flask framework for web development
- ORB algorithm developers for feature detection

## 📞 Contact

For questions or support, please open an issue on GitHub or contact the maintainers.

---

**Note**: This system works best with clear, well-lit face images and detailed sketches. Results may vary based on image quality and sketch accuracy.


