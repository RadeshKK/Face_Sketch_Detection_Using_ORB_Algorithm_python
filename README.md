# Face_Sketch_Detection_Using_ORB_Algorithm_python

Extract features for each real face image and the sketch image.
Data Input:
User uploads real face images (folder) and a sketch image (single file).
Feature Extraction:
Use ORB (Oriented FAST and Rotated BRIEF) to detect keypoints and compute descriptors for both real images and the sketch.
Feature Storage:
Store extracted descriptors (as binary blobs), image paths, and names in an SQLite database.
Matching Algorithm:
Use BFMatcher to compare sketch descriptors with stored descriptors.
Sort matches by distance and calculate similarity percentages.
Result Ranking:
Identify and rank top N matches based on similarity scores.
Web Interface:
Use Flask for the web app to handle file uploads and display results.


