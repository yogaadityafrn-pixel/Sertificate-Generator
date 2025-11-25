📜 Sertifikat-Generator
Generate Sertifikat Super Cepat dengan Python

Proyek ini adalah sebuah skrip Python sederhana yang secara otomatis menambahkan nama peserta ke template sertifikat. Nama-nama peserta diambil dari file CSV, kemudian diproses dan ditempelkan pada gambar sertifikat yang telah disiapkan. Hasil akhir dari proses ini adalah file PDF yang berisi sertifikat untuk setiap peserta.

✨ Fitur Utama
Membaca nama-nama peserta dari file peserta.csv.

Menempatkan nama pada gambar sertifikat (sertif.png) dengan posisi dan ukuran font yang disesuaikan secara otomatis.

Menyimpan sertifikat yang sudah diproses sebagai file PDF dalam folder hasil/.

🛠️ Prasyarat
Pastikan Anda telah menginstal Python 3.8 atau versi lebih baru serta library yang diperlukan sebelum menjalankan skrip:

Instalasi Library
Gunakan pip untuk menginstal library PIL (Pillow) dan pandas:

1. PIL (Python Imaging Library):

pip install pillow

2. pandas:

pip install pandas

🚀 Cara Penggunaan
Ikuti langkah-langkah di bawah untuk menghasilkan sertifikat.

1. Persiapan File
Pastikan semua file berikut berada di dalam satu direktori yang sama dengan skrip Python (generate_sertif.py):

2. Jalankan Skrip
Buka Terminal atau Command Prompt, lalu navigasikan ke direktori tempat skrip berada.

Jalankan perintah berikut:

python generate_sertif.py

Skrip akan memproses nama-nama dari file CSV dan menghasilkan file PDF sertifikat untuk setiap peserta.

3. Cek Hasil
Setelah proses selesai, semua sertifikat akan tersimpan di dalam folder hasil dengan nama file berdasarkan nama peserta yang bersangkutan (misalnya, Yoga Aditya Fernanda.pdf).
