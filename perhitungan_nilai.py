# Konfigurasi disimpan di folder yang sama dengan program
FILE_BOBOT = "bobot_penilaian.txt"

BOBOT_DEFAULT = {
    "partisipasi": 0.05, "proyek": 0.45, "tugas": 0.05,
    "quis": 0.05, "uts": 0.20, "uas": 0.20
}

def muat_bobot():
    """Memuat bobot dari file. Jika tidak ada, gunakan bobot default."""
    try:
        with open(FILE_BOBOT, "r") as file:
            data = file.read().strip().split("|")
            if len(data) == 6:
                return {
                    "partisipasi": float(data[0]),
                    "proyek": float(data[1]),
                    "tugas": float(data[2]),
                    "quis": float(data[3]),
                    "uts": float(data[4]),
                    "uas": float(data[5])
                }
    except (FileNotFoundError, ValueError):
        pass
    return dict(BOBOT_DEFAULT)

def simpan_bobot(bobot):
    """Menyimpan pengaturan bobot baru ke dalam file txt."""
    with open(FILE_BOBOT, "w") as file:
        teks = f"{bobot['partisipasi']}|{bobot['proyek']}|{bobot['tugas']}|{bobot['quis']}|{bobot['uts']}|{bobot['uas']}"
        file.write(teks)

def hitung_nilai_akhir(partisipasi, proyek, tugas, quis, uts, uas, bobot=None):
    """Menghitung nilai akhir sesuai bobot. Jika bobot tidak diberikan, dibaca dari file."""
    if bobot is None:
        bobot = muat_bobot()
    akhir = (partisipasi * bobot['partisipasi']) + \
            (proyek * bobot['proyek']) + \
            (tugas * bobot['tugas']) + \
            (quis * bobot['quis']) + \
            (uts * bobot['uts']) + \
            (uas * bobot['uas'])
    return akhir

def tentukan_grade(nilai):
    """Menentukan huruf grade berdasarkan nilai akhir"""
    if nilai >= 85: return "A"
    elif nilai >= 70: return "B"
    elif nilai >= 55: return "C"
    elif nilai >= 40: return "D"
    else: return "E"

def tentukan_status(grade):
    """Menentukan status kelulusan"""
    if grade in ("A", "B", "C"): return "LULUS"
    return "TIDAK LULUS"