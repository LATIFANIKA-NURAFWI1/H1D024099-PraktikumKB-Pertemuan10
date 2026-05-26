

import random
import matplotlib.pyplot as plt

# Import modul-modul yang telah dibuat
from inisialisasi_populasi import inisialisasi_populasi
from evaluasi_fitness import barang, kapasitas_gudang, hitung_fitness
from selection import roulette_wheel_selection, tournament_selection
from crossover import one_point_crossover, two_point_crossover, uniform_crossover
from mutation import swap_mutation, inversion_mutation, uniform_mutation

def pilih_seleksi(digit_pertama: str) -> str:
    """Digit pertama: 0,2,4,6,8 -> RWS; 1,3,5,7,9 -> TS"""
    return "RWS" if int(digit_pertama) % 2 == 0 else "TS"

def pilih_crossover(digit_kedua: str) -> str:
    """Pemetaan digit kedua ke metode crossover (sesuai tabel modul)"""
    tabel = {
        '0': 'one_point', '1': 'two_point', '2': 'uniform',
        '3': 'one_point', '4': 'two_point', '5': 'uniform',
        '6': 'one_point', '7': 'two_point', '8': 'uniform',
        '9': 'one_point'
    }
    return tabel.get(digit_kedua, 'one_point')

def pilih_mutasi(dua_digit: str) -> str:
    """Jumlah dua digit, ambil digit terakhir, lalu petakan ke metode mutasi"""
    total = int(dua_digit[0]) + int(dua_digit[1])
    digit_akhir = total % 10
    tabel = {
        0: 'swap', 1: 'inversion', 2: 'uniform',
        3: 'swap', 4: 'inversion', 5: 'uniform',
        6: 'swap', 7: 'inversion', 8: 'uniform',
        9: 'swap'
    }
    return tabel[digit_akhir]

def info_metode(dua_digit: str):
    d1, d2 = dua_digit[0], dua_digit[1]
    sel = pilih_seleksi(d1)
    cro = pilih_crossover(d2)
    mut = pilih_mutasi(dua_digit)
    nama_sel = "Roulette Wheel Selection" if sel == "RWS" else "Tournament Selection"
    nama_cro = {
        'one_point': 'One-Point Crossover',
        'two_point': 'Two-Point Crossover',
        'uniform': 'Uniform Crossover'
    }[cro]
    nama_mut = {
        'swap': 'Swap Mutation',
        'inversion': 'Inversion Mutation',
        'uniform': 'Uniform Mutation'
    }[mut]
    total = int(d1) + int(d2)
    print("=" * 50)
    print(f"  Dua digit terakhir NIM : {dua_digit}")
    print(f"  Digit pertama [{d1}]  → Seleksi  : {nama_sel}")
    print(f"  Digit kedua   [{d2}]  → Crossover: {nama_cro}")
    print(f"  {d1}+{d2} = {total} → digit terakhir {total%10} → Mutasi   : {nama_mut}")
    print("=" * 50)
    return sel, cro, mut

def run_ga(metode_seleksi, metode_crossover, metode_mutasi,
           jumlah_generasi=50, jumlah_populasi=20,
           prob_crossover=0.8, prob_mutasi=0.1):
    
    jumlah_gen = len(barang)
    
    # 1. Inisialisasi populasi
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    
    print("\nNilai Fitness:")
    fitness_populasi = [hitung_fitness(ind, barang, kapasitas_gudang) for ind in populasi]
    for idx in range(min(3, len(fitness_populasi))):
        print(f"Individu {idx+1}: Fitness = {fitness_populasi[idx]}")
    
    # Pilih parent1
    parent1, idx1 = None, None
    if metode_seleksi == "RWS":
        parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)
    else:
        parent1, idx1 = tournament_selection(populasi, fitness_populasi)
    
    # Pilih parent2 dari sisa
    avail_idx = [i for i in range(len(populasi)) if i != idx1]
    avail_pop = [populasi[i] for i in avail_idx]
    avail_fit = [fitness_populasi[i] for i in avail_idx]
    if metode_seleksi == "RWS":
        parent2, local_idx = roulette_wheel_selection(avail_pop, avail_fit)
    else:
        parent2, local_idx = tournament_selection(avail_pop, avail_fit)
    parent2_idx = avail_idx[local_idx]
    
    # Konversi parent ke nama indeks untuk tampilan (misal individu1, individu2)
    print("\nParent Terpilih:")
    print(f"Parent 1: individu{idx1+1}")
    print(f"Parent 2: individu{parent2_idx+1}")
    
    # Crossover untuk mendapatkan anak
    if random.random() < prob_crossover:
        anak1, anak2 = None, None
        if metode_crossover == "one_point":
            anak1, anak2 = one_point_crossover(parent1, parent2)
        elif metode_crossover == "two_point":
            anak1, anak2 = two_point_crossover(parent1, parent2)
        else:
            anak1, anak2 = uniform_crossover(parent1, parent2)
    else:
        anak1, anak2 = parent1[:], parent2[:]
    
    print("\nAnak Hasil Crossover:")
    print(f"Anak 1: {anak1}")
    print(f"Anak 2: {anak2}")
    
    contoh_anak = anak1.copy()
    print("\nAnak Setelah Mutasi:")
    print(f"Anak 1 (Swap Mutation): {swap_mutation(contoh_anak.copy())}")
    print(f"Anak 2 (Inversion Mutation): {inversion_mutation(contoh_anak.copy())}")
    print(f"Anak 3 (Uniform Mutation): {uniform_mutation(contoh_anak.copy())}")
    
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []
    best_individu = None
    best_overall = 0
    
    for generasi in range(jumlah_generasi):
        fitness_populasi = [hitung_fitness(ind, barang, kapasitas_gudang) for ind in populasi]
        
        best_f = max(fitness_populasi)
        worst_f = min(fitness_populasi)
        avg_f = sum(fitness_populasi) / len(fitness_populasi)
        best_fitness_list.append(best_f)
        worst_fitness_list.append(worst_f)
        avg_fitness_list.append(avg_f)
        all_fitness.append(fitness_populasi.copy())
        
        if best_f > best_overall:
            best_overall = best_f
            best_individu = populasi[fitness_populasi.index(best_f)][:]
        
        # Membentuk populasi baru
        new_populasi = []
        while len(new_populasi) < jumlah_populasi:
            # Seleksi parent1
            if metode_seleksi == "RWS":
                p1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)
            else:
                p1, idx1 = tournament_selection(populasi, fitness_populasi)
            # Seleksi parent2 (berbeda)
            avail_idx = [i for i in range(len(populasi)) if i != idx1]
            avail_pop = [populasi[i] for i in avail_idx]
            avail_fit = [fitness_populasi[i] for i in avail_idx]
            if metode_seleksi == "RWS":
                p2, local_idx = roulette_wheel_selection(avail_pop, avail_fit)
            else:
                p2, local_idx = tournament_selection(avail_pop, avail_fit)
            # Crossover
            if random.random() < prob_crossover:
                if metode_crossover == "one_point":
                    a1, a2 = one_point_crossover(p1, p2)
                elif metode_crossover == "two_point":
                    a1, a2 = two_point_crossover(p1, p2)
                else:
                    a1, a2 = uniform_crossover(p1, p2)
            else:
                a1, a2 = p1[:], p2[:]
            # Mutasi
            if random.random() < prob_mutasi:
                if metode_mutasi == "swap":
                    a1 = swap_mutation(a1)
                elif metode_mutasi == "inversion":
                    a1 = inversion_mutation(a1)
                else:
                    a1 = uniform_mutation(a1, prob_mutasi)
            if random.random() < prob_mutasi:
                if metode_mutasi == "swap":
                    a2 = swap_mutation(a2)
                elif metode_mutasi == "inversion":
                    a2 = inversion_mutation(a2)
                else:
                    a2 = uniform_mutation(a2, prob_mutasi)
            new_populasi.extend([a1, a2])
        populasi = new_populasi[:jumlah_populasi]
    
    # Plot grafik
    plt.figure(figsize=(12, 7))
    for i in range(jumlah_generasi):
        x = [i+1] * len(all_fitness[i])
        plt.scatter(x, all_fitness[i], color='gray', alpha=0.15, s=18)
    plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', linewidth=2, label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi+1), avg_fitness_list, color='red', linewidth=2, label='Fitness Rata-rata')
    plt.plot(range(1, jumlah_generasi+1), worst_fitness_list, color='#FFD700', linewidth=2, label='Fitness Terendah')
    sel_nama = "Roulette Wheel" if metode_seleksi == "RWS" else "Tournament"
    cro_nama = {"one_point":"One-Point","two_point":"Two-Point","uniform":"Uniform"}[metode_crossover]
    mut_nama = metode_mutasi.capitalize()
    plt.title(f"Perkembangan Nilai Fitness (NIM: {nim_input})\nSeleksi: {sel_nama} | Crossover: {cro_nama} | Mutasi: {mut_nama}", fontsize=13, fontweight='bold')
    plt.xlabel("Generasi")
    plt.ylabel("Nilai Fitness (Keuntungan)")
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()
    
    # Hasil akhir
    terpilih = [barang[i][0] for i in range(jumlah_gen) if best_individu[i] == 1]
    total_keuntungan = hitung_fitness(best_individu, barang, kapasitas_gudang)
    total_ukuran = sum(barang[i][2] for i in range(jumlah_gen) if best_individu[i] == 1)
    print("\n=== HASIL OPTIMASI GUDANG ===\n")
    print(f"Total Keuntungan (Fitness Terbaik) : {total_keuntungan}")
    print(f"Total Ukuran                       : {total_ukuran} / {kapasitas_gudang}")
    print("Barang Terpilih:")
    for item in terpilih:
        print(f"  - {item}")

if __name__ == "__main__":
    print("\n=== PROGRAM ALGORITMA GENETIKA UNTUK KNAPSACK PROBLEM ===\n")
    while True:
        nim_input = input("Masukkan NIM lengkap atau dua digit terakhir NIM: ").strip()
        if len(nim_input) >= 2:
            dua_digit = nim_input[-2:]
            if dua_digit.isdigit():
                break
        print("Input tidak valid. Pastikan dua digit terakhir adalah angka.\n")
    
    metode_seleksi, metode_crossover, metode_mutasi = info_metode(dua_digit)
    
    run_ga(
        metode_seleksi=metode_seleksi,
        metode_crossover=metode_crossover,
        metode_mutasi=metode_mutasi,
        jumlah_generasi=50,
        jumlah_populasi=20,
        prob_crossover=0.8,
        prob_mutasi=0.1
    )