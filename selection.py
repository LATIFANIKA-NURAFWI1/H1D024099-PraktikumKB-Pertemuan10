import random

def roulette_wheel_selection(populasi, fitness_populasi):
    """Roulette Wheel Selection: pilih berdasarkan proporsi fitness."""
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx
    prob = [f / total_fitness for f in fitness_populasi]
    kumulatif = 0
    for i, p in enumerate(prob):
        kumulatif += p
        if random.random() <= kumulatif:
            return populasi[i], i
    return populasi[-1], len(populasi) - 1

def tournament_selection(populasi, fitness_populasi, k=3):
    """Tournament Selection: pilih k acak, ambil fitness tertinggi."""
    k = min(k, len(populasi))
    peserta_idx = random.sample(range(len(populasi)), k)
    best_idx = max(peserta_idx, key=lambda i: fitness_populasi[i])
    return populasi[best_idx], best_idx

if __name__ == "__main__":
    # Contoh penggunaan
    populasi_awal = ['individu1', 'individu2', 'individu3', 'individu4']
    fitness_populasi = [10, 20, 30, 40]
    parent1, idx1 = roulette_wheel_selection(populasi_awal, fitness_populasi)
    
    # Hapus parent1
    avail_pop = populasi_awal[:idx1] + populasi_awal[idx1+1:]
    avail_fit = fitness_populasi[:idx1] + fitness_populasi[idx1+1:]
    parent2, _ = tournament_selection(avail_pop, avail_fit)
    print("\nParent Terpilih:")
    print(f"Parent 1: {parent1}")
    print(f"Parent 2: {parent2}")