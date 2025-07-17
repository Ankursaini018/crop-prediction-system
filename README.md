# 🌾 Smart Crop Recommendation System

A machine learning-powered web application that suggests the most suitable crop to grow based on environmental and soil parameters. Designed to assist farmers and agronomists in making informed decisions to improve agricultural productivity.

---

## 🌟 Features

* ✅ **Real-time Crop Recommendation** based on soil nutrients, temperature, humidity, rainfall, and pH.
* 🧠 **Trained ML Model** using scikit-learn for accurate crop prediction.
* 🌍 **Intuitive Web Interface** built with Flask and Jinja2 templates.
* 🖼️ **Visual Crop Gallery** showing crop images to enhance user understanding.
* 📖 **Informative Pages**: Home, About, Project, Contact, and History sections.
* 🧪 **Integrated Notebook** (`.ipynb`) for model training and performance analysis.

---

## 📂 Project Structure

├── app.py # Flask application entry point
├── model.joblib # Trained ML model (joblib serialized)
├── crop.csv # Raw crop data
├── crop\_clean.csv # Preprocessed data for training
├── Crop recommendation.ipynb # Jupyter Notebook for EDA & model training
├── templates/ # HTML files (Home, About, Contact, etc.)
│ ├── index.html
│ ├── about.html
│ ├── project.html
│ ├── contact.html
│ ├── history.html
│ └── layout.html
├── static/ # Images and assets
│ └── \[crop images and visuals]
