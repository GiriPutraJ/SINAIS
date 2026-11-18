# SINAIS - Sistem Informasi Nilai Akademis Mahasiswa

SINAIS ini program CLI buatan Python buat ngelola data dan nilai mahasiswa. Dibuat untuk Tugas Project Akhir Praktikum Dasar Pemrograman, dan perhitungan nilainya mengikuti Kontrak Perkuliahan Elektronika TA 2025-2026.

## Fitur

- CRUD: tambah, lihat, edit, dan hapus data mahasiswa.
- Cari data berdasarkan NIM (pakai linear search).
- Urutkan data pakai bubble sort, bisa berdasarkan nilai akhir (tertinggi ke terendah) atau nama (A-Z).
- Validasi kehadiran. Maksimal 14 pertemuan, dan kalau hadir kurang dari 11 pertemuan (bolos lebih dari 3x) mahasiswa tidak boleh ikut UAS, jadi nilai UAS otomatis 0.
- Nilai akhir dihitung sesuai kontrak kuliah dengan bobot:
  - Aktivitas partisipatif 5%
  - Hasil proyek 45%
  - Tugas 5%
  - Quis 5%
  - UTS 20%
  - UAS 20%
- Nilai akhir dikonversi ke huruf mutu (A-E), status lulus/tidak, dan IPK skala 4.0.
- Data disimpan ke file `data_mahasiswa.txt`, jadi tidak hilang waktu program ditutup.

## Konsep yang dipakai

- List of dictionary buat nyimpen data mahasiswa di memori.
- Fungsi dan modul terpisah supaya kodenya tidak numpuk di satu file.
- Searching dan sorting (linear search dan bubble sort).
- Pengolahan string, misalnya f-string, `.strip()`, `.split()`, dan `.lower()`.

## Struktur file

```
main.py               # program utama, menu CLI dan alur operasi
perhitungan_nilai.py  # hitung nilai akhir, grade, dan status kelulusan
perhitungan_ipk.py    # konversi grade ke IPK dan rata-rata IPK kelas
data_mahasiswa.txt    # tempat data disimpan
README.md             # dokumentasi ini
```

## Cara menjalankan

1. Pastikan Python 3 sudah terinstal.
2. Buka terminal atau Command Prompt, lalu masuk ke folder project ini.
3. Jalankan:

```bash
python main.py
```