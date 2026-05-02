# 🌿 Sugarcane Disease Detection using Deep Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat-square&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Project Overview

An **image-based machine learning system** for the automated detection, classification, and identification of sugarcane leaf diseases. This project leverages a **Convolutional Neural Network (CNN)** model trained on sugarcane leaf images to accurately distinguish between healthy and diseased crops, helping farmers take timely action to prevent yield loss.

The system is deployed via a **Streamlit web application**, enabling users to upload leaf images and receive instant disease predictions with high accuracy.

---

## ✨ Features

- 🔍 **Automated Disease Detection** – Upload a leaf image and get an instant diagnosis
- 🧠 **Deep Learning Classification** – CNN model trained on real sugarcane leaf datasets
- 🌾 **Multi-Class Disease Identification** – Detects 5 categories including healthy leaves
- 📊 **Confidence Score** – Displays prediction confidence for each classification
- 🖥️ **Interactive Web Interface** – Simple and intuitive Streamlit-based UI
- ⚡ **Fast Inference** – Real-time predictions with minimal latency

---

## 🦠 Diseases Detected

| Class | Description |
|-------|-------------|
| ✅ **Healthy** | No disease detected — normal leaf |
| 🔴 **Red Rot** | Caused by *Colletotrichum falcatum*; red discoloration inside stalks |
| 🟤 **Rust** | Caused by *Puccinia melanocephala*; orange-brown pustules on leaves |
| 🟡 **Yellow** | Yellowing of leaves due to nutrient deficiency or viral infection |
| 🟣 **Mosaic** | Viral disease causing mosaic-like discoloration patterns on leaves |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| Deep Learning | TensorFlow / Keras |
| Model Architecture | Convolutional Neural Network (CNN) |
| Web Application | Streamlit |
| Image Processing | OpenCV / PIL |
| Model Storage | HDF5 (`.h5` format) |

---

## 📁 Project Structure

```
sugarcane-disease-detection/
│
├── dataset/                  # Training and validation image dataset
├── app.py                    # Streamlit web application
├── train.py                  # Model training script
├── predict.py                # Prediction/inference script
├── sugarcane_model.h5        # Trained CNN model
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ashishwaliya19/sugarcane-disease-detection.git
   cd sugarcane-disease-detection
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Running the Web Application

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`.

### Training the Model

```bash
python train.py
```

> Make sure your dataset is organized in subdirectories by class inside the `dataset/` folder before training.

### Running Predictions via Script

```bash
python predict.py --image path/to/leaf_image.jpg
```

### How to Use the Web App

1. Launch the Streamlit app using the command above
2. Click **"Browse files"** to upload a sugarcane leaf image (JPG/PNG)
3. Click **"Predict"** to analyze the image
4. View the **predicted disease class** and **confidence score**

---

## 🧪 Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Input Size:** 224 × 224 × 3 (RGB images)
- **Output Classes:** 5 (Healthy, RedRot, Rust, Yellow, Mosaic)
- **Framework:** TensorFlow / Keras
- **Saved Format:** `.h5` (HDF5)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate comments.

---


---

## 👨‍💻 Author

Developed as part of a research project on **image-based machine learning approaches for agricultural disease detection**.

---

> ⭐ If you found this project helpful, please consider giving it a star!