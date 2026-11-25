import perhitungan_nilai as pn
import perhitungan_ipk as pi

NAMA_FILE = "data_mahasiswa.txt"
LEBAR = 75
PANJANG_NIM = 11

def judul(teks):
    print("\n" + "=" * LEBAR)
    print(teks.center(LEBAR))
    print("=" * LEBAR)

def cetak_tabel(data):
    print(f"{'NIM':<14}{'Nama':<20}{'Hadir':<8}{'Proyek':<8}{'Akhir':<8}{'Grade':<7}{'Status'}")
    print("-" * LEBAR)
    for m in data:
        print(f"{m['nim']:<14}{m['nama']:<20}{m['hadir']:<8}{m['proyek']:<8.2f}{m['akhir']:<8.2f}{m['grade']:<7}{m['status']}")
    print("-" * LEBAR)

def muat_data():
    data = []
    try:
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
    except FileNotFoundError:
        pass
    return data

def simpan_data(data):
    with open(NAMA_FILE, "w") as file:
        for m in data:
            teks = f"{m['nim']}|{m['nama']}|{m['hadir']}|{m['partisipasi']}|{m['proyek']}|{m['tugas']}|{m['quis']}|{m['uts']}|{m['uas']}|{m['akhir']}|{m['grade']}|{m['status']}|{m['ipk']}\n"
            file.write(teks)

def nim_valid(nim):
    return len(nim) == PANJANG_NIM and nim[0].isalpha() and nim[1:].isdigit()

def input_nim(label="  NIM   : "):
    while True:
        nim = input(label).strip().upper()
        if nim_valid(nim):
            return nim
        print("  ! Format NIM salah. Contoh yang benar: J0404261234 (1 huruf + 10 angka).")

def nama_valid(nama):
    if nama == "":
        print("  ! Nama tidak boleh kosong.")
        return False
    if "|" in nama or "," in nama:
        print("  ! Nama tidak boleh mengandung karakter '|' atau ','.")
        return False
    return True

def input_nama(label="  Nama  : "):
    while True:
        nama = " ".join(input(label).split())
        if nama_valid(nama):
            return nama.title()

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

def urutkan_berdasarkan_nim(data):
    hasil = data[:]
    for i in range(1, len(hasil)):
        kunci = hasil[i]
        j = i - 1
        while j >= 0 and hasil[j]['nim'] > kunci['nim']:
            hasil[j + 1] = hasil[j]
            j -= 1
        hasil[j + 1] = kunci
    return hasil

def binary_search_nim(data_terurut, nim):
    kiri, kanan = 0, len(data_terurut) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data_terurut[tengah]['nim'] == nim:
            return data_terurut[tengah]
        elif data_terurut[tengah]['nim'] < nim:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return None

def linear_search_nama(data, kata):
    kata = kata.lower()
    hasil = []
    for m in data:
        if kata in m['nama'].lower():
            hasil.append(m)
    return hasil

def cari_data(data):
    judul("CARI DATA MAHASISWA")
    if not data:
        print("Belum ada data.")
        return
    print("1. Cari berdasarkan NIM (Binary Search)")
    print("2. Cari berdasarkan Nama (Linear Search, sebagian nama)")
    pilihan = input("Pilih metode (1/2): ").strip()

    if pilihan == "1":
        nim_cari = input("Masukkan NIM yang dicari: ").strip().upper()
        terurut = urutkan_berdasarkan_nim(data)
        m = binary_search_nim(terurut, nim_cari)
        if m:
            print("\n  ✓ Data Ditemukan!")
            print(f"    NIM         : {m['nim']}\n    Nama        : {m['nama']}\n    Kehadiran   : {m['hadir']}/14")
            print(f"    Nilai Akhir : {m['akhir']:.2f}\n    Grade       : {m['grade']} ({m['status']})\n    IPK         : {m['ipk']:.2f}")
        else:
            print("  ! Data mahasiswa tidak ditemukan.")
    elif pilihan == "2":
        kata = input("Masukkan nama / sebagian nama: ").strip()
        if kata == "":
            print("  ! Kata pencarian tidak boleh kosong.")
            return
        hasil = linear_search_nama(data, kata)
        if hasil:
            print(f"\n  ✓ Ditemukan {len(hasil)} data:\n")
            cetak_tabel(hasil)
        else:
            print("  ! Tidak ada nama yang cocok.")
    else:
        print("  ! Pilihan tidak valid.")

def urutkan_data(data):
    judul("URUTKAN DATA MAHASISWA")
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

def hitung_ulang(m, bobot=None):
    m['akhir'] = pn.hitung_nilai_akhir(m['partisipasi'], m['proyek'], m['tugas'], m['quis'], m['uts'], m['uas'], bobot)
    m['grade'] = pn.tentukan_grade(m['akhir'])
    m['status'] = pn.tentukan_status(m['grade'])
    m['ipk'] = pi.konversi_grade_ke_ip(m['grade'])

def tambah_data(data):
    judul("TAMBAH DATA MAHASISWA")
    nim = input_nim()

    for m in data:
        if m['nim'] == nim:
            print("  ! Gagal: Mahasiswa dengan NIM tersebut sudah ada.")
            return

    nama = input_nama()
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

    m = {
        "nim": nim, "nama": nama, "hadir": hadir,
        "partisipasi": partisipasi, "proyek": proyek, "tugas": tugas, "quis": quis,
        "uts": uts, "uas": uas
    }
    hitung_ulang(m, bobot)
    data.append(m)
    simpan_data(data)
    print("  ✓ Data berhasil ditambahkan dan disimpan!")

def tampilkan_data(data):
    judul("DATA MAHASISWA")
    if not data:
        print("Belum ada data.")
        return

    cetak_tabel(data)
    rata_ipk = pi.hitung_rata_rata_ipk(data)
    print(f"Total: {len(data)} mahasiswa  |  Rata-rata IPK Kelas: {rata_ipk:.2f}")

def edit_data(data):
    judul("EDIT DATA MAHASISWA")
    nim = input("Masukkan NIM yang ingin diedit: ").strip().upper()

    for m in data:
        if m['nim'] == nim:
            print(f"Data ditemukan: {m['nama']}")
            while True:
                nama_baru = " ".join(input(f"  Nama baru ({m['nama']}), Enter = tetap: ").split())
                if nama_baru == "":
                    break
                if nama_valid(nama_baru):
                    m['nama'] = nama_baru.title()
                    break

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

            hitung_ulang(m, bobot)
            simpan_data(data)
            print("  ✓ Data berhasil diperbarui dan disimpan!")
            return

    print("  ! Mahasiswa dengan NIM tersebut tidak ditemukan.")

def hapus_data(data):
    judul("HAPUS DATA MAHASISWA")
    nim = input("Masukkan NIM yang ingin dihapus: ").strip().upper()
    for i, m in enumerate(data):
        if m['nim'] == nim:
            konfirmasi = input(f"Yakin ingin menghapus data {m['nama']}? (y/n): ")
            if konfirmasi.lower() == 'y':
                del data[i]
                simpan_data(data)
                print("  ✓ Data berhasil dihapus dan disimpan!")
            else:
                print("  Penghapusan dibatalkan.")
            return
    print("  ! Mahasiswa dengan NIM tersebut tidak ditemukan.")

def atur_bobot(data):
    judul("PENGATURAN BOBOT PENILAIAN")
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
                hitung_ulang(m, bobot_baru)
            simpan_data(data)
            print("  ✓ Seluruh database telah disinkronkan dengan bobot yang baru!")
    except ValueError:
        print("  ! Input gagal. Harap masukkan angka yang valid.")

def statistik_kelas(data):
    judul("DASHBOARD STATISTIK KELAS")
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
    print(f"Jumlah TIDAK LULUS: {tidak_lulus} Orang")
    print(f"Rata-rata IPK     : {rata_ipk:.2f}")
    print("-" * 40)
    print(f"Mahasiswa Terbaik : {nilai_tertinggi['nama']} (Nilai: {nilai_tertinggi['akhir']:.2f})")
    print(f"Nilai Terendah   : {nilai_terendah['nama']} (Nilai: {nilai_terendah['akhir']:.2f})")

def export_ke_csv(data):
    judul("EXPORT DATA KE EXCEL (CSV)")
    if not data:
        print("Belum ada data untuk diexport.")
        return

    nama_file_csv = "laporan_nilai_kelas.csv"

    try:
        with open(nama_file_csv, "w") as file:
            file.write("NIM,Nama,Kehadiran,Partisipasi,Proyek,Tugas,Quis,UTS,UAS,Nilai Akhir,Grade,Status,IPK\n")
            for m in data:
                file.write(f"{m['nim']},{m['nama']},{m['hadir']},{m['partisipasi']},{m['proyek']},{m['tugas']},{m['quis']},{m['uts']},{m['uas']},{m['akhir']},{m['grade']},{m['status']},{m['ipk']}\n")
        print("  ✓ SUCCESS: Data berhasil diexport!")
        print(f"  ✓ Silakan cek file '{nama_file_csv}' di folder program.")
    except Exception as e:
        print(f"  ! Gagal melakukan export: {e}")

def main():
    data_mahasiswa = muat_data()

    while True:
        judul("SINAIS: MENU UTAMA")
        print("  1. Tambah Data Mahasiswa")
        print("  2. Tampilkan Data & IPK")
        print("  3. Edit Data")
        print("  4. Hapus Data")
        print("  5. Cari Data Mahasiswa (Searching)")
        print("  6. Urutkan Data (Sorting)")
        print("  7. Pengaturan Bobot Penilaian (Dinamis)")
        print("  8. Dashboard Statistik Kelas")
        print("  9. Export Data ke Excel (CSV)")
        print(" 10. Keluar")
        print("-" * LEBAR)

        pilihan = input("Pilih menu (1-10): ").strip()

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