import random

def swap_mutation(kromosom):
    kromosom = list(kromosom)
    i, j = random.sample(range(len(kromosom)), 2)
    kromosom[i], kromosom[j] = kromosom[j], kromosom[i]
    return kromosom

def inversion_mutation(kromosom):
    kromosom = list(kromosom)
    i = random.randint(0, len(kromosom)-2)
    j = random.randint(i+1, len(kromosom)-1)
    kromosom[i:j] = reversed(kromosom[i:j])
    return kromosom

def uniform_mutation(kromosom, mutation_rate=0.1):
    kromosom = list(kromosom)
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]
    return kromosom

if __name__ == "__main__":
    anak1 = [0, 1, 1, 0, 1]
    print("\nAnak Setelah Mutasi:")
    print(f"Anak 1 (Swap Mutation): {swap_mutation(anak1.copy())}")
    print(f"Anak 2 (Inversion Mutation): {inversion_mutation(anak1.copy())}")
    print(f"Anak 3 (Uniform Mutation): {uniform_mutation(anak1.copy())}")