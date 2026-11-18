def konversi_grade_ke_ip(grade):
    """Mengubah nilai huruf menjadi nilai mutu angka (skala 4.0)"""
    if grade == "A": return 4.0
    elif grade == "B": return 3.0
    elif grade == "C": return 2.0
    elif grade == "D": return 1.0
    else: return 0.0

def hitung_rata_rata_ipk(data_mahasiswa):
    """Menghitung rata-rata IPK seluruh data mahasiswa"""
    if not data_mahasiswa:
        return 0.0
    
    total_ip = 0
    for m in data_mahasiswa:
        total_ip += m['ipk']
        
    return total_ip / len(data_mahasiswa)