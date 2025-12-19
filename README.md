# 🌸 Aurora Fake News Detector

Aplikasi web modern dan futuristik untuk deteksi berita palsu menggunakan Machine Learning (Naive Bayes) dengan tema Aurora Pink-Orange Gradient.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![ML](https://img.shields.io/badge/ML-Naive%20Bayes-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-96%25+-brightgreen.svg)

## ✨ Fitur Utama

- 🤖 **Machine Learning**: Algoritma Naive Bayes dengan TF-IDF vectorization
- 📊 **Akurasi Tinggi**: Model dengan akurasi ~96%+
- 🎨 **UI Modern**: Desain futuristik dengan glassmorphism dan aurora gradient
- 📱 **Responsive**: Perfect di mobile dan desktop
- ⚡ **Real-time**: Prediksi instan dalam hitungan detik
- 📈 **Visualisasi**: Gallery visualisasi data dan performa model
- 🌐 **Bahasa Indonesia**: Interface 100% dalam Bahasa Indonesia

## 🎨 Tema Visual

- **Warna Utama**: Pink Neon (#FF6B9D), Coral, Peach, Orange (#FFA500)
- **Style**: Glassmorphism, Neon Glow, Aurora Gradient
- **Animasi**: Smooth transitions, hover effects, micro-interactions
- **Font**: Inter & Space Grotesk (Google Fonts)

## 🚀 Instalasi & Menjalankan

### 1. Clone atau Download Project

```bash
cd TUGAS_12
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Favicon (Opsional)

```bash
python create_favicon.py
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## 📁 Struktur Project

```
TUGAS_12/
├── app.py                              # Flask backend
├── fake_real_news_nb_pipeline.joblib   # Model ML
├── requirements.txt                     # Dependencies
├── Procfile                            # Railway deployment
├── create_favicon.py                   # Favicon generator
├── templates/
│   ├── base.html                       # Base template
│   ├── home.html                       # Landing page
│   ├── predict.html                    # Halaman prediksi
│   ├── visualizations.html             # Gallery visualisasi
│   ├── about.html                      # Tentang proyek
│   └── contact.html                    # Kontak
├── static/
│   ├── css/
│   │   └── style.css                   # Comprehensive styling
│   ├── js/
│   │   └── app.js                      # Interactions & animations
│   ├── plots/                          # Folder visualisasi
│   ├── favicon.ico                     # Favicon
│   ├── favicon.png                     # Favicon PNG
│   └── favicon.svg                     # Favicon SVG
└── README.md
```

## 🎯 Cara Menggunakan

### 1. **Beranda**
- Lihat overview fitur dan statistik
- Klik "Mulai Prediksi" untuk memulai

### 2. **Prediksi**
- Masukkan teks berita (minimal 50 karakter)
- Atau gunakan tombol "Contoh Fake" / "Contoh Real"
- Klik "Prediksi Sekarang"
- Lihat hasil dengan confidence score dan probabilitas

### 3. **Visualisasi**
- Tambahkan file gambar (.png, .jpg, .svg) ke folder `static/plots/`
- Visualisasi akan muncul otomatis dalam gallery
- Klik gambar untuk memperbesar

### 4. **Tentang**
- Pelajari cara kerja Naive Bayes
- Lihat informasi dataset dan akurasi model

### 5. **Kontak**
- Kirim feedback atau pertanyaan
- Lihat informasi kontak

## 🚀 Deploy ke Railway

### 1. Persiapan

Pastikan file berikut ada:
- `requirements.txt` ✓
- `Procfile` ✓
- `fake_real_news_nb_pipeline.joblib` ✓

### 2. Deploy

1. Push project ke GitHub
2. Buka [Railway.app](https://railway.app)
3. Login dan klik "New Project"
4. Pilih "Deploy from GitHub repo"
5. Pilih repository Anda
6. Railway akan otomatis detect Flask dan deploy

### 3. Environment Variables (Opsional)

Tidak ada environment variables yang diperlukan untuk setup dasar.

## 🤖 Tentang Model

- **Algoritma**: Multinomial Naive Bayes
- **Preprocessing**: TF-IDF Vectorization
- **Dataset**: ~40,000+ artikel (Fake & Real News)
- **Akurasi**: ~96%+
- **Label**: 
  - 0 = Fake (Berita Palsu)
  - 1 = Real (Berita Asli)

## 🎨 Teknologi

- **Backend**: Flask (Python)
- **ML Library**: scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS dengan Glassmorphism
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Deployment**: Railway + Gunicorn

## 📊 Fitur Teknis

### Backend
- Model loading saat startup
- Input validation & sanitization
- Flash messages untuk notifikasi
- Error handling
- Dynamic visualization loading

### Frontend
- Aurora gradient animated background
- Glassmorphism cards
- Smooth page transitions
- Hover effects & micro-interactions
- Progress bar animations
- Modal lightbox untuk visualisasi
- Responsive navbar dengan mobile menu
- Auto-hide navbar on scroll
- Character counter untuk textarea
- Loading states

### Animasi
- Fade-in-up untuk elements
- Aurora background movement
- Floating particles
- Card tilt on hover
- Button ripple effect
- Progress bar fill animation
- Badge pulse animation
- Smooth scroll

## 🎯 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📝 Catatan

- Model dilatih dengan dataset bahasa Inggris
- Untuk hasil terbaik, gunakan teks berita dalam bahasa Inggris
- Minimal 50 karakter, maksimal 10,000 karakter
- Prediksi bersifat probabilistik, gunakan sebagai referensi

## 🤝 Kontribusi

Project ini dibuat untuk tugas Machine Learning. Feedback dan saran sangat diterima!

## 📄 Lisensi

Educational Project - 2024

## 🌟 Credits

- **Design**: Aurora Pink-Orange Gradient Theme
- **ML Model**: Naive Bayes with TF-IDF
- **Dataset**: Fake & Real News Dataset
- **Framework**: Flask
- **Deployment**: Railway

---

**Dibuat dengan ❤️ menggunakan Flask, Python, dan Machine Learning**

🌸 Aurora Fake News Detector - Deteksi Berita Palsu dengan Kecerdasan Buatan 🌸
