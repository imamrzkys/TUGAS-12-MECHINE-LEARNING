import os
from flask import Flask, render_template, request, flash, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'aurora-fake-news-detector-2024-secret-key'

model = None
MODEL_PATH = 'fake_real_news_nb_pipeline.joblib'

def load_model():
    global model
    try:
        model = joblib.load(MODEL_PATH)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

load_model()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form.get('news_text', '').strip()
        
        if not news_text:
            flash('Mohon masukkan teks berita untuk diprediksi.', 'error')
            return redirect(url_for('predict'))
        
        if len(news_text) < 50:
            flash('Teks berita terlalu pendek. Minimal 50 karakter.', 'error')
            return redirect(url_for('predict'))
        
        if len(news_text) > 10000:
            flash('Teks berita terlalu panjang. Maksimal 10.000 karakter.', 'error')
            return redirect(url_for('predict'))
        
        if model is None:
            flash('Model belum dimuat. Silakan coba lagi.', 'error')
            return redirect(url_for('predict'))
        
        try:
            prediction = model.predict([news_text])[0]
            probabilities = model.predict_proba([news_text])[0]
            
            prob_fake = probabilities[0] * 100
            prob_real = probabilities[1] * 100
            
            result = {
                'prediction': 'REAL' if prediction == 1 else 'FAKE',
                'prediction_label': 'Berita Asli' if prediction == 1 else 'Berita Palsu',
                'confidence': max(prob_fake, prob_real),
                'prob_fake': prob_fake,
                'prob_real': prob_real,
                'text': news_text
            }
            
            if result['confidence'] >= 90:
                result['interpretation'] = 'Sangat Yakin'
            elif result['confidence'] >= 60:
                result['interpretation'] = 'Cukup Yakin'
            else:
                result['interpretation'] = 'Ragu-ragu'
            
            return render_template('predict.html', result=result)
        
        except Exception as e:
            flash(f'Terjadi kesalahan saat prediksi: {str(e)}', 'error')
            return redirect(url_for('predict'))
    
    return render_template('predict.html', result=None)

@app.route('/visualizations')
def visualizations():
    plots_dir = os.path.join('static', 'plots')
    plot_files = []
    
    if os.path.exists(plots_dir):
        for filename in os.listdir(plots_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
                caption = filename.replace('_', ' ').replace('-', ' ').rsplit('.', 1)[0].title()
                plot_files.append({
                    'filename': filename,
                    'path': f'plots/{filename}',
                    'caption': caption
                })
    
    return render_template('visualizations.html', plots=plot_files)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()
        
        if not name or not email or not message:
            flash('Mohon lengkapi semua field.', 'error')
            return redirect(url_for('contact'))
        
        flash('Pesan Anda berhasil dikirim! Terima kasih atas feedback Anda.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
