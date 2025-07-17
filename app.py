from flask import Flask, render_template, request, redirect, url_for, flash, session
import joblib
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

# Load the trained model
MODEL_PATH = 'model.joblib'
model = joblib.load(MODEL_PATH)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Project page
@app.route('/project', methods=['GET'])
def project():
    prediction = session.pop('prediction', None)
    return render_template('project.html', prediction=prediction)

# History page
@app.route('/history')
def history():
    return render_template('history.html', history=session.get('history', []))

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Farming/AI info page
@app.route('/farming')
def farming():
    return render_template('farming.html')

# Crop recommendation form and result
@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = model.predict(features)[0]
        # Map number to crop name if needed
        label_map = {
            1: 'rice', 2: 'maize', 3: 'jute', 4: 'cotton', 5: 'coconut', 6: 'papaya', 7: 'orange', 8: 'apple',
            9: 'muskmelon', 10: 'watermelon', 11: 'grapes', 12: 'mango', 13: 'banana', 14: 'pomegranate',
            15: 'lentil', 16: 'blackgram', 17: 'mungbean', 18: 'mothbeans', 19: 'pigeonpeas', 20: 'kidneybeans',
            21: 'chickpea', 22: 'coffee'
        }
        if isinstance(prediction, (int, np.integer)) and prediction in label_map:
            prediction_name = label_map[prediction]
        else:
            prediction_name = str(prediction)
        # Image logic
        crop_images = {
            'rice': '/static/crop_rice.jpg',
            'wheat': '/static/crop_wheat.jpg',
            'maize': '/static/crop_maize.jpg',
            'potato': '/static/crop_potato.jpg',
            'sugarcane': '/static/crop_sugarcane.jpg',
            'cotton': '/static/crop_cotton.jpg',
            'barley': '/static/crop_barley.jpg',
            'millet': '/static/crop_millet.jpg',
            'peas': '/static/crop_peas.jpg',
            'banana': '/static/crop_banana.jpg',
            'mango': '/static/crop_mango.jpg',
            'apple': '/static/crop_apple.jpg',
            'orange': '/static/crop_orange.jpg',
            'grapes': '/static/crop_grapes.jpg',
            'coconut': '/static/crop_coconut.jpg',
            'coffee': '/static/crop_coffee.jpg',
            'jute': '/static/crop_jute.jpg',
            'lentil': '/static/crop_lentil.jpg',
            'kidneybeans': '/static/crop_kidneybeans.jpg',
            'pigeonpeas': '/static/crop_pigeonpeas.jpg',
            'chickpea': '/static/crop_chickpea.jpg',
            'mothbeans': '/static/crop_mothbeans.jpg',
            'mungbean': '/static/crop_mungbean.jpg',
            'blackgram': '/static/crop_blackgram.jpg',
            'muskmelon': '/static/crop_muskmelon.jpg',
            'watermelon': '/static/crop_watermelon.jpg',
            'papaya': '/static/crop_papaya.jpg',
            'pomegranate': '/static/crop_pomegranate.jpg',
        }
        crop_key = prediction_name.lower()
        if crop_key in crop_images:
            crop_img = crop_images[crop_key]
        else:
            crop_img = f'https://source.unsplash.com/400x400/?{crop_key},crop,field,plant'
        # Store in session history
        history = session.get('history', [])
        history.insert(0, {
            'crop': prediction_name,
            'image': crop_img,
            'time': datetime.now().strftime('%d %b %Y, %I:%M %p')
        })
        session['history'] = history[:20]  # Keep only last 20
        # Pass prediction to /project
        session['prediction'] = prediction_name
        return redirect(url_for('project'))
    except Exception as e:
        flash('Invalid input or error in prediction: {}'.format(e), 'danger')
        return redirect(url_for('project'))

# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
