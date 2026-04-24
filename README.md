# Dashboard Analisis Penyewaan Sepeda

Dashboard ini dibuat menggunakan Streamlit untuk menampilkan hasil analisis data penyewaan sepeda berdasarkan beberapa faktor seperti cuaca, waktu (jam), dan jenis hari (hari kerja vs akhir pekan).

## Fitur Dashboard
Dashboard ini memiliki beberapa fitur utama:
- Visualisasi pengaruh cuaca terhadap jumlah penyewaan sepeda
- Analisis pola penyewaan berdasarkan jam
- Perbandingan penyewaan antara hari kerja dan akhir pekan
- Fitur filter berdasarkan tahun
- Download dataset (clean dan raw data)

---

## Akses Dashboard Online
Dashboard dapat diakses melalui link berikut: https://submission-datasetbike.streamlit.app/ 

---

## Cara Menjalankan Dashboard Secara Lokal
Ikuti langkah-langkah berikut untuk menjalankan dashboard di komputer lokal:

### 1. Clone Repository

```bash
git clone https://github.com/Anitawidyastini/submission.git
```

### 2. Install Dependencies

Pastikan Python sudah terinstall (disarankan versi 3.9–3.11), kemudian install semua library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi Streamlit

Masuk ke folder project dan jalankan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

### 4. Akses Dashboard

Setelah berhasil dijalankan, buka browser dan akses:

```
http://localhost:8501
```

Dashboard akan otomatis tampil di halaman tersebut.