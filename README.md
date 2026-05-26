# Algoritma Genetika untuk Knapsack Problem – Praktikum KB Pertemuan 10

> **Optimasi Pemilihan Barang dengan Algoritma Genetika**  
> Berbasis pemetaan metode seleksi, crossover, dan mutasi dari NIM mahasiswa.

---

## Identitas Praktikan

| Nama      | [Nama Lengkap]           |
| ----------| ------------------------ |
| **Nama**  | [Latifani kaNurafwi]     |
| **NIM**   | [H1D024099]              |

---

## Deskripsi Program

Program ini menyelesaikan **Knapsack Problem** (masalah memilih barang dengan keuntungan maksimal dalam kapasitas terbatas) menggunakan **Algoritma Genetika** (AG).  

**Data barang (5 item):**

| Barang   | Keuntungan | Ukuran |
|----------|------------|--------|
| Barang1  | 10         | 5      |
| Barang2  | 40         | 4      |
| Barang3  | 30         | 6      |
| Barang4  | 50         | 3      |
| Barang5  | 35         | 7      |

**Kapasitas gudang:** 15

**Parameter GA:**
- Jumlah generasi: 50
- Jumlah populasi: 20
- Probabilitas crossover: 0.8
- Probabilitas mutasi: 0.1

---

- **Input NIM** – User memasukkan NIM, program secara otomatis memilih metode seleksi, crossover, dan mutasi sesuai aturan modul.
- **Modular** – Setiap komponen GA dipisah ke file sendiri (`inisialisasi_populasi.py`, `evaluasi_fitness.py`, `selection.py`, `crossover.py`, `mutation.py`).
- **Output detail** – Menampilkan:
  - Nilai fitness 3 individu awal.
  - Parent terpilih (contoh seleksi).
  - Hasil crossover dari parent tersebut.
  - Contoh mutasi (swap, inversion, uniform) pada salah satu anak.
- **Grafik perkembangan fitness** – Menampilkan garis fitness tertinggi, rata-rata, terendah, dan titik-titik semua individu per generasi.
- **Hasil akhir** – Barang terpilih, total keuntungan, total ukuran.

---

## Instalasi & Persiapan

### 1. Pastikan Python terinstal (versi 3.7+)
```bash
python --version
```

### 2. Install library yang diperlukan (hanya matplotlib)
```bash
pip install matplotlib
```

### 3. Letakkan semua file dalam satu folder
Pastikan file berikut ada:
- `inisialisasi_populasi.py`
- `evaluasi_fitness.py`
- `selection.py`
- `crossover.py`
- `mutation.py`
- `main.py`

---

## Cara Menjalankan

Buka terminal di folder tersebut, lalu jalankan:

```bash
python main.py
```

Kemudian masukkan NIM (cukup dua digit terakhir atau NIM lengkap).  
Contoh input: `H1D024099` atau `99`.

Program akan berjalan dan menampilkan output secara bertahap, serta grafik di akhir.

---

## Struktur File & Penjelasan Kode

| File | Fungsi |
|------|--------|
| `inisialisasi_populasi.py` | Membangkitkan populasi awal berupa kromosom biner acak. Fungsi: `inisialisasi_populasi(jumlah_populasi, jumlah_gen)` |
| `evaluasi_fitness.py` | Menyimpan data barang, kapasitas, dan fungsi `hitung_fitness(kromosom, barang, kapasitas)`. Fitness = total keuntungan jika total ukuran ≤ kapasitas, selain itu 0 (penalti). |
| `selection.py` | Implementasi Roulette Wheel Selection dan Tournament Selection. Masing-masing mengembalikan (individu, indeks). |
| `crossover.py` | Metode crossover: `one_point_crossover`, `two_point_crossover`, `uniform_crossover`. Masing-masing mengembalikan dua anak. |
| `mutation.py` | Metode mutasi: `swap_mutation`, `inversion_mutation`, `uniform_mutation`. |
| `main.py` | File utama: menerima input NIM, memetakan metode berdasarkan aturan modul, menjalankan GA, menampilkan output detail dan grafik. |

---

## Aturan Pemetaan Metode dari NIM

### Seleksi (digit pertama dua digit terakhir)
- Genap (0,2,4,6,8) → **Roulette Wheel Selection (RWS)**
- Ganjil (1,3,5,7,9) → **Tournament Selection (TS)**

### Crossover (digit kedua)
| Digit | Metode Crossover |
|-------|------------------|
| 0,3,6,9 | One-Point |
| 1,4,7   | Two-Point |
| 2,5,8   | Uniform |

### Mutasi (digit terakhir dari penjumlahan dua digit)
Jumlahkan dua digit, ambil digit terakhir hasil penjumlahan.  
Contoh: `2+4=6` → digit terakhir 6 → **Swap Mutation**

| Digit akhir | Metode Mutasi |
|-------------|----------------|
| 0,3,6,9     | Swap           |
| 1,4,7       | Inversion      |
| 2,5,8       | Uniform        |

---

*(Nilai sebenarnya dapat berbeda karena proses acak)*

---
## Contoh Output

### Hasil akhir (contoh)
```
=============================================
=== PROGRAM ALGORITMA GENETIKA UNTUK KNAPSACK PROBLEM ===

Masukkan NIM lengkap atau dua digit terakhir NIM: H1D024099
==================================================
  Dua digit terakhir NIM : 99
  Digit pertama [9]  → Seleksi  : Tournament Selection
  Digit kedua   [9]  → Crossover: One-Point Crossover
  9+9 = 18 → digit terakhir 8 → Mutasi   : Uniform Mutation
==================================================

Nilai Fitness:
Individu 1: Fitness = 85
Individu 2: Fitness = 0
Individu 3: Fitness = 60

Parent Terpilih:
Parent 1: individu19
Parent 2: individu1

Anak Hasil Crossover:
Anak 1: [0, 1, 0, 0, 0]
Anak 2: [0, 0, 0, 1, 1]

Anak Setelah Mutasi:
Anak 1 (Swap Mutation): [1, 0, 0, 0, 0]
Anak 2 (Inversion Mutation): [0, 1, 0, 0, 0]
Anak 3 (Uniform Mutation): [0, 1, 0, 1, 0]

=== HASIL OPTIMASI GUDANG ===

Total Keuntungan (Fitness Terbaik) : 125
Total Ukuran                       : 14 / 15
Barang Terpilih:
  - Barang2
  - Barang4
  - Barang5
=============================================
```

## Grafik yang Dihasilkan

Grafik menampilkan:
- **Garis biru** – fitness tertinggi setiap generasi.
- **Garis merah** – fitness rata-rata.
- **Garis kuning** – fitness terendah.
- **Titik abu-abu** – semua nilai fitness individu di setiap generasi (makin gelap = makin banyak individu dengan fitness serupa).

Judul grafik akan mencantumkan **dua digit NIM** yang diinput user dan metode yang digunakan.

---
