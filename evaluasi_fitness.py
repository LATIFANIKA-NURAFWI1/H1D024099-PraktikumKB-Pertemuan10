# Data barang (nama, keuntungan, ukuran) untuk Pertemuan 10
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7),
]

kapasitas_gudang = 15  # Ukuran maksimal gudang

def hitung_fitness(kromosom, barang, kapasitas):
    """
    Menghitung fitness = total keuntungan jika total ukuran <= kapasitas,
    selain itu fitness = 0 (penalti).
    """
    total_keuntungan = 0
    total_ukuran = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_keuntungan += barang[i][1]
            total_ukuran += barang[i][2]
    if total_ukuran > kapasitas:
        return 0
    return total_keuntungan

if __name__ == "__main__":
    # Contoh penggunaan
    populasi_awal = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
    ]
    print("\nNilai Fitness:")
    for idx, individu in enumerate(populasi_awal):
        fitness = hitung_fitness(individu, barang, kapasitas_gudang)
        print(f"Individu {idx+1}: Fitness = {fitness}")