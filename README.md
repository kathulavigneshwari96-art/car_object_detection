# 🚗 Car Object Detection using Computer Vision

## 📌 Project Overview
This project is a Car Object Detection system developed using Python, OpenCV, and Computer Vision techniques.

The system detects cars in images using bounding box annotations from the dataset and highlights detected vehicles with rectangles.

It also counts the total number of detected cars in each image.

---

## 🎯 Features
- Multiple car detection
- Bounding box visualization
- Car counting system
- Output image generation
- Batch image processing
- Detection result visualization

---

## 🛠 Technologies Used
- Python
- OpenCV
- Pandas
- Matplotlib

---

## 📂 Dataset Structure

car_object_detection/
│
├── data/
│   ├── training_images/
│   ├── testing_images/
│   ├── cars.csv
│   └── sample_submission.csv
│
├── outputs/
├── detection.py
└── README.md

---

## 📦 Dataset Information
The dataset contains:
- Training images
- Testing images
- Bounding box annotation CSV file

### CSV Annotation Format

| image | xmin | ymin | xmax | ymax |
|------|------|------|------|------|

These coordinates are used to locate cars inside images.

---

## ⚙️ Installation

Install required libraries:

```bash
pip install pandas opencv-python matplotlib
