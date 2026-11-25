# SINAIS - Sistem Informasi Nilai Akademis Mahasiswa

SINAIS ini program CLI buatan Python buat ngelola data dan nilai mahasiswa. Dibuat untuk Tugas Project Akhir Praktikum Dasar Pemrograman, dan perhitungan nilainya mengikuti Kontrak Perkuliahan Dasar Pemograman 2026-2027.

Program jalan di terminal, tanpa GUI, tanpa database, dan tanpa library tambahan (cuma pakai bawaan Python).

## Fitur

- CRUD: tambah, lihat, edit, dan hapus data mahasiswa.
- Cari data mahasiswa:
  - Berdasarkan NIM, pakai binary search (data diurutkan dulu pakai insertion sort).
  - Berdasarkan nama atau sebagian nama, pakai linear search, tidak peduli huruf besar/kecil.
- Urutkan data pakai bubble sort, bisa berdasarkan nilai akhir (tertinggi ke terendah) atau nama (A-Z).
- Validasi input:
  - NIM harus berformat 1 huruf + 10 angka, contoh `J0404261234`. Huruf otomatis jadi kapital.
  - Nama tidak boleh kosong dan tidak boleh mengandung karakter `|` atau `,`. Nama otomatis dirapikan jadi huruf kapital di awal kata.
  - Nilai harus 0-100, kehadiran harus 0-14.
- Validasi kehadiran. Maksimal 14 pertemuan, dan kalau hadir kurang dari 11 pertemuan (bolos lebih dari 3x) mahasiswa tidak boleh ikut UAS, jadi nilai UAS otomatis 0.
- Bobot penilaian default sesuai kontrak kuliah, tapi bisa diubah lewat menu pengaturan bobot (total harus 100%). Kalau bobot diubah, semua nilai mahasiswa otomatis dihitung ulang.

  | Komponen | Bobot default |
  |---|---|
  | Aktivitas partisipatif | 5% |
  | Hasil proyek | 45% |
  | Tugas | 5% |
  | Quis | 5% |
  | UTS | 20% |
  | UAS | 20% |

- Nilai akhir dikonversi ke huruf mutu, status lulus/tidak, dan IPK skala 4.0:

  | Nilai akhir | Grade | IPK | Status |
  |---|---|---|---|
  | 85 ke atas | A | 4.0 | LULUS |
  | 70 - 84 | B | 3.0 | LULUS |
  | 55 - 69 | C | 2.0 | LULUS |
  | 40 - 54 | D | 1.0 | TIDAK LULUS |
  | di bawah 40 | E | 0.0 | TIDAK LULUS |

- Dashboard statistik kelas: total mahasiswa, jumlah lulus dan tidak lulus, rata-rata IPK, mahasiswa terbaik, dan nilai terendah.
- Export data ke file CSV (`laporan_nilai_kelas.csv`) yang bisa dibuka di Excel.
- Data disimpan ke file `.txt`, jadi tidak hilang waktu program ditutup.

## Konsep yang dipakai

- Tipe data koleksi: list of dictionary buat data mahasiswa di memori, dan dictionary buat bobot penilaian.
- Fungsi dan modul terpisah supaya kodenya tidak numpuk di satu file.
- Searching dan sorting: linear search, binary search, bubble sort, dan insertion sort.
- Pengolahan string: f-string, `.strip()`, `.split()`, `.join()`, `.lower()`, `.upper()`, `.title()`, `.isdigit()`, `.isalpha()`, dan operator `in`.
- Penyimpanan data ke file teks dengan penanganan error (`try` dan `except`).

## Struktur file

```
main.py                  program utama, menu CLI dan alur operasi
perhitungan_nilai.py     bobot, hitung nilai akhir, grade, dan status kelulusan
perhitungan_ipk.py       konversi grade ke IPK dan rata-rata IPK kelas
data_mahasiswa.txt       tempat data mahasiswa disimpan (dibuat otomatis)
bobot_penilaian.txt      tempat bobot penilaian disimpan (dibuat otomatis)
laporan_nilai_kelas.csv  hasil export data (dibuat otomatis)
README.md                dokumentasi ini
```

## Anggota kelompok

| Nama | Persentase pengerjaan |
|---|---|
| Giri | 40% |
| Ghazi | 30% |
| Rivaldo | 30% |

## Cara menjalankan

1. Pastikan Python 3 sudah terinstal.
2. Buka terminal atau Command Prompt, lalu masuk ke folder project ini.
3. Jalankan:

```bash
python main.py
```

4. Pilih menu 1-10 sesuai kebutuhan. File data akan dibuat otomatis di folder yang sama.

## Menu utama

1. Tambah Data Mahasiswa
2. Tampilkan Data & IPK
3. Edit Data
4. Hapus Data
5. Cari Data Mahasiswa (Searching)
6. Urutkan Data (Sorting)
7. Pengaturan Bobot Penilaian (Dinamis)
8. Dashboard Statistik Kelas
9. Export Data ke Excel (CSV)
10. Keluar