import os
import perhitungan_nilai as pn
import perhitungan_ipk as pi

NAMA_FILE = "data/data_mahasiswa.txt"

def pastikan_folder_ada():
    """Memastikan folder 'data' otomatis dibuat jika belum ada"""
    if not os.path.exists("data"):
        os.makedirs("data")

def muat_data():
    pastikan_folder_ada()
    data = []
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                item = baris.strip().split("|")
                if len(item) == 13:
                    data.append({
                        "nim": item[0], "nama": item[1], "hadir": int(item[2]), 
                        "partisipasi": float(item[3]), "proyek": float(item[4]),
                        "tugas": float(item[5]), "quis": float(item[6]),
                        "uts": float(item[7]), "uas": float(item[8]),
                        "akhir": float(item[9]), "grade": item[10], 
                        "status": item[11], "ipk": float(item[12])
                    })
    return data

def simpan_data(data):
    pastikan_folder_ada()
    with open(NAMA_FILE, "w") as file:
        for m in data:
            teks = f"{m['nim']}|{m['nama']}|{m['hadir']}|{m['partisipasi']}|{m['proyek']}|{m['tugas']}|{m['quis']}|{m['uts']}|{m['uas']}|{m['akhir']}|{m['grade']}|{m['status']}|{m['ipk']}\n"
            file.write(teks)

def input_nilai_valid(label):
    while True:
        try:
            nilai = float(input(f"  Masukkan {label}: "))
            if 0 <= nilai <= 100:
                return nilai
            print("  ! Nilai harus di antara 0 dan 100.")
        except ValueError:
            print("  ! Input harus berupa angka.")

def input_kehadiran():
    while True:
        try:
            hadir = int(input("  Masukkan Jumlah Kehadiran (maks 14): "))
            if 0 <= hadir <= 14:
                return hadir
            print("  ! Kehadiran maksimal adalah 14 pertemuan.")
        except ValueError:
            print("  ! Input harus berupa angka bulat.")

def tambah_data(data):
    print("\n--- TAMBAH DATA MAHASISWA ---")
    nim = input("  NIM   : ")
    
    for m in data:
        if m['nim'] == nim:
            print("  ! Gagal: Mahasiswa dengan NIM tersebut sudah ada.")
            return

    nama = input("  Nama  : ")
    hadir = input_kehadiran()
    
    bobot = pn.muat_bobot()
    
    partisipasi = input_nilai_valid(f"Nilai Partisipasi ({int(bobot['partisipasi']*100)}%)")
    proyek = input_nilai_valid(f"Nilai Proyek ({int(bobot['proyek']*100)}%)")
    tugas = input_nilai_valid(f"Nilai Tugas ({int(bobot['tugas']*100)}%)")
    quis = input_nilai_valid(f"Nilai Quis ({int(bobot['quis']*100)}%)")
    uts = input_nilai_valid(f"Nilai UTS ({int(bobot['uts']*100)}%)")
    
    if hadir < 11:
        print(f"  ! Peringatan: Kehadiran hanya {hadir}/14 (Bolos lebih dari 3x).")
        print("  ! Mahasiswa TIDAK diizinkan mengikuti UAS. Nilai UAS otomatis 0.")
        uas = 0.0
    else:
        uas = input_nilai_valid(f"Nilai UAS ({int(bobot['uas']*100)}%)")

    akhir = pn.hitung_nilai_akhir(partisipasi, proyek, tugas, quis, uts, uas)
    grade = pn.tentukan_grade(akhir)
    status = pn.tentukan_status(grade)
    ipk = pi.konversi_grade_ke_ip(grade)

    data.append({
        "nim": nim, "nama": nama, "hadir": hadir,
        "partisipasi": partisipasi, "proyek": proyek, "tugas": tugas, "quis": quis,
        "uts": uts, "uas": uas,
        "akhir": akhir, "grade": grade, "status": status, "ipk": ipk
    })
    simpan_data(data)
    print("  ✓ Data berhasil ditambahkan dan disimpan!")

def tampilkan_data(data):
    print("\n--- DATA MAHASISWA ---")
    if not data:
        print("Belum ada data.")
        return
        
    print(f"{'NIM':<10}{'Nama':<15}{'Hadir':<8}{'Proyek':<8}{'Akhir':<8}{'Grade':<8}{'Status'}")
    print("-" * 65)
    for m in data:
        print(f"{m['nim']:<10}{m['nama']:<15}{m['hadir']:<8}{m['proyek']:<8.2f}{m['akhir']:<8.2f}{m['grade']:<8}{m['status']}")
    
    rata_ipk = pi.hitung_rata_rata_ipk(data)
    print("-" * 65)
    print(f"Rata-rata IPK Kelas: {rata_ipk:.2f}")

def edit_data(data):
    print("\n--- EDIT DATA MAHASISWA ---")
    nim = input("Masukkan NIM yang ingin diedit: ")
    
    for m in data:
        if m['nim'] == nim:
            print(f"Data ditemukan: {m['nama']}")
            m['nama'] = input(f"  Nama baru ({m['nama']}): ") or m['nama']
            
            m['hadir'] = input_kehadiran()
            bobot = pn.muat_bobot()
            
            m['partisipasi'] = input_nilai_valid(f"Nilai Partisipasi baru ({int(bobot['partisipasi']*100)}%)")
            m['proyek'] = input_nilai_valid(f"Nilai Proyek baru ({int(bobot['proyek']*100)}%)")
            m['tugas'] = input_nilai_valid(f"Nilai Tugas baru ({int(bobot['tugas']*100)}%)")
            m['quis'] = input_nilai_valid(f"Nilai Quis baru ({int(bobot['quis']*100)}%)")
            m['uts'] = input_nilai_valid(f"Nilai UTS baru ({int(bobot['uts']*100)}%)")
            
            if m['hadir'] < 11:
                print(f"  ! Peringatan: Kehadiran hanya {m['hadir']}/14.")
                print("  ! Mahasiswa TIDAK diizinkan mengikuti UAS. Nilai UAS otomatis 0.")
                m['uas'] = 0.0
            else:
                m['uas'] = input_nilai_valid(f"Nilai UAS baru ({int(bobot['uas']*100)}%)")
            
            m['akhir'] = pn.hitung_nilai_akhir(m['partisipasi'], m['proyek'], m['tugas'], m['quis'], m['uts'], m['uas'])
            m['grade'] = pn.tentukan_grade(m['akhir'])
            m['status'] = pn.tentukan_status(m['grade'])
            m['ipk'] = pi.konversi_grade_ke_ip(m['grade'])
            
            simpan_data(data)
            print("  ✓ Data berhasil diperbarui dan disimpan!")
            return
            
    print("  ! Mahasiswa dengan NIM tersebut tidak ditemukan.")

def hapus_data(data):
    print("\n--- HAPUS DATA MAHASISWA ---")
    nim = input("Masukkan NIM yang ingin dihapus: ")
    for i, m in enumerate(data):
        if m['nim'] == nim:
            konfirmasi = input(f"Yakin ingin menghapus data {m['nama']}? (y/n): ")
            if konfirmasi.lower() == 'y':
                del data[i]
                simpan_data(data)
                print("  ✓ Data berhasil dihapus dan disimpan!")
            return
    print("  ! Mahasiswa dengan NIM tersebut tidak ditemukan.")

def cari_data(data):
    print("\n--- CARI DATA MAHASISWA ---")
    if not data:
        print("Belum ada data.")
        return
    nim_cari = input("Masukkan NIM yang dicari: ")
    ditemukan = False
    for m in data:
        if m['nim'] == nim_cari:
            print("\n  ✓ Data Ditemukan!")
            print(f"    NIM         : {m['nim']}\n    Nama        : {m['nama']}\n    Kehadiran   : {m['hadir']}/14")
            print(f"    Nilai Akhir : {m['akhir']:.2f}\n    Grade       : {m['grade']} ({m['status']})\n    IPK         : {m['ipk']:.2f}")
            ditemukan = True
            break
    if not ditemukan:
        print("  ! Data mahasiswa tidak ditemukan.")

def urutkan_data(data):
    print("\n--- URUTKAN DATA MAHASISWA (SORTING) ---")
    if not data:
        print("Belum ada data.")
        return
    print("1. Berdasarkan Nilai Akhir Tertinggi (Ranking)\n2. Berdasarkan Nama (A-Z)")
    pilihan = input("Pilih metode urut (1/2): ")
    n = len(data)
    if pilihan == '1':
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j]['akhir'] < data[j+1]['akhir']:
                    data[j], data[j+1] = data[j+1], data[j]
        print("  ✓ Data berhasil diurutkan berdasarkan Ranking!")
    elif pilihan == '2':
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j]['nama'].lower() > data[j+1]['nama'].lower():
                    data[j], data[j+1] = data[j+1], data[j]
        print("  ✓ Data berhasil diurutkan berdasarkan Abjad Nama!")
    else:
        print("  ! Pilihan tidak valid.")
        return
    simpan_data(data)
    tampilkan_data(data)

def atur_bobot(data):
    print("\n--- PENGATURAN BOBOT PENILAIAN ---")
    print("Masukkan bobot baru dalam angka persen (contoh: 20 untuk 20%).")
    print("Syarat: Total keseluruhan harus tepat 100%!")
    try:
        partisipasi = float(input("\n  Bobot Partisipasi (%) : ")) / 100
        proyek = float(input("  Bobot Proyek (%)      : ")) / 100
        tugas = float(input("  Bobot Tugas (%)       : ")) / 100
        quis = float(input("  Bobot Quis (%)        : ")) / 100
        uts = float(input("  Bobot UTS (%)         : ")) / 100
        uas = float(input("  Bobot UAS (%)         : ")) / 100
        
        total = partisipasi + proyek + tugas + quis + uts + uas
        
        if round(total, 2) != 1.00:
            print(f"  ! GAGAL: Total bobot saat ini {total*100:.0f}%. Syarat tidak terpenuhi.")
            return
            
        bobot_baru = {
            "partisipasi": partisipasi, "proyek": proyek, "tugas": tugas,
            "quis": quis, "uts": uts, "uas": uas
        }
        pn.simpan_bobot(bobot_baru)
        print("\n  ✓ Bobot penilaian berhasil diperbarui dan disimpan!")
        
        if data:
            print("  ! Sistem sedang mengkalkulasi ulang seluruh nilai mahasiswa...")
            for m in data:
                m['akhir'] = pn.hitung_nilai_akhir(m['partisipasi'], m['proyek'], m['tugas'], m['quis'], m['uts'], m['uas'])
                m['grade'] = pn.tentukan_grade(m['akhir'])
                m['status'] = pn.tentukan_status(m['grade'])
                m['ipk'] = pi.konversi_grade_ke_ip(m['grade'])
            simpan_data(data)
            print("  ✓ Seluruh database telah disinkronkan dengan bobot yang baru!")
    except ValueError:
        print("  ! Input gagal. Harap masukkan angka yang valid.")

def statistik_kelas(data):
    print("\n--- DASHBOARD STATISTIK KELAS ---")
    if not data:
        print("Belum ada data mahasiswa.")
        return

    total_mahasiswa = len(data)
    lulus = 0
    tidak_lulus = 0
    nilai_tertinggi = data[0]
    nilai_terendah = data[0]

    for m in data:
        if m['status'] == "LULUS":
            lulus += 1
        else:
            tidak_lulus += 1
            
        if m['akhir'] > nilai_tertinggi['akhir']:
            nilai_tertinggi = m
        if m['akhir'] < nilai_terendah['akhir']:
            nilai_terendah = m

    rata_ipk = pi.hitung_rata_rata_ipk(data)

    print(f"Total Mahasiswa   : {total_mahasiswa} Orang")
    print(f"Jumlah LULUS      : {lulus} Orang")
    print(f"Jumlah REMEDIAL   : {tidak_lulus} Orang")
    print(f"Rata-rata IPK     : {rata_ipk:.2f}")
    print("-" * 35)
    print(f"🏆 Mahasiswa Terbaik : {nilai_tertinggi['nama']} (Nilai: {nilai_tertinggi['akhir']:.2f})")
    print(f"⚠️ Nilai Terendah   : {nilai_terendah['nama']} (Nilai: {nilai_terendah['akhir']:.2f})")

def export_ke_csv(data):
    print("\n--- EXPORT DATA KE EXCEL (CSV) ---")
    if not data:
        print("Belum ada data untuk diexport.")
        return
        
    pastikan_folder_ada()
    nama_file_csv = "data/laporan_nilai_kelas.csv"

    try:
        with open(nama_file_csv, "w") as file:
            file.write("NIM,Nama,Kehadiran,Partisipasi,Proyek,Tugas,Quis,UTS,UAS,Nilai Akhir,Grade,Status,IPK\n")
            for m in data:
                file.write(f"{m['nim']},{m['nama']},{m['hadir']},{m['partisipasi']},{m['proyek']},{m['tugas']},{m['quis']},{m['uts']},{m['uas']},{m['akhir']},{m['grade']},{m['status']},{m['ipk']}\n")
        print(f"  ✓ SUCCESS: Data berhasil diexport!")
        print(f"  ✓ Silakan cek file '{nama_file_csv}' di dalam folder data.")
    except Exception as e:
        print(f"  ! Gagal melakukan export: {e}")

def main():
    data_mahasiswa = muat_data()
    
    while True:
        print("\n===== SINAIS: MENU UTAMA =====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data & IPK")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Cari Data Mahasiswa (Searching)")
        print("6. Urutkan Data (Sorting)")
        print("7. Pengaturan Bobot Penilaian (Dinamis)")
        print("8. Dashboard Statistik Kelas")
        print("9. Export Data ke Excel (CSV)")
        print("10. Keluar")
        
        pilihan = input("Pilih menu (1-10): ")
        
        if pilihan == "1": tambah_data(data_mahasiswa)
        elif pilihan == "2": tampilkan_data(data_mahasiswa)
        elif pilihan == "3": edit_data(data_mahasiswa)
        elif pilihan == "4": hapus_data(data_mahasiswa)
        elif pilihan == "5": cari_data(data_mahasiswa)
        elif pilihan == "6": urutkan_data(data_mahasiswa)
        elif pilihan == "7": atur_bobot(data_mahasiswa)
        elif pilihan == "8": statistik_kelas(data_mahasiswa)
        elif pilihan == "9": export_ke_csv(data_mahasiswa)
        elif pilihan == "10":
            print("Terima kasih telah menggunakan SINAIS. Program selesai.")
            break
        else:
            print("! Pilihan tidak valid.")

if __name__ == "__main__":
    main()