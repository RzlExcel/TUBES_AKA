import random
import time

# Struktur pemain
class Player:
    def __init__(self, name, trophy):
        self.name = name
        self.trophy = trophy

# Fungsi rekursif untuk mencocokkan musuh berdasarkan trophy
def find_enemies_recursive(player_trophies, ranges, num_enemies, index=0, enemy_index=1):
    if index >= len(player_trophies):  # Basis rekursif: jika semua pemain diproses
        return []

    enemies = []
    trophy = player_trophies[index]

    # Temukan grup berdasarkan trophy
    for r in ranges:
        if r[0] <= trophy <= r[1]:
            # Tambahkan musuh secara random di grup yang sesuai
            for _ in range(num_enemies // len(player_trophies)):
                enemy_trophy = random.randint(r[0], r[1])
                enemies.append(Player(name=f"Enemy{enemy_index}", trophy=enemy_trophy))
                enemy_index += 1
            break

    # Rekursif untuk pemain berikutnya
    return enemies + find_enemies_recursive(player_trophies, ranges, num_enemies, index + 1, enemy_index)

# Fungsi iteratif untuk mencocokkan musuh berdasarkan trophy
def find_enemies_iterative(player_trophies, ranges, num_enemies):
    enemies = []

    for trophy in player_trophies:
        for r in ranges:
            if r[0] <= trophy <= r[1]:
                for _ in range(num_enemies // len(player_trophies)):
                    enemy_trophy = random.randint(r[0], r[1])
                    enemies.append(Player(name=f"Enemy{len(enemies) + 1}", trophy=enemy_trophy))
                break

    return enemies

def main():
    # Inisialisasi random seed
    random.seed()

    # Input jumlah pemain
    num_players = int(input("Masukkan jumlah pemain (1 atau 2): "))

    # Validasi input jumlah pemain (hanya 1 atau 2 yang diterima)
    if num_players not in [1, 2]:
        print("Jumlah pemain harus 1 atau 2. Program akan berhenti.")
        return

    # Tentukan jumlah musuh berdasarkan jumlah pemain
    num_enemies = 8  # Default for 2 players
    if num_players == 1:
        num_enemies = 9  # For 1 player, we need 9 enemies

    # Input trophy untuk setiap pemain
    player_trophies = []
    for i in range(1, num_players + 1):
        trophy = int(input(f"Masukkan trophy untuk pemain {i}: "))

        # Check if the trophy exceeds 1000
        if trophy > 1000:
            print("Trophy tidak boleh lebih dari 1000. Program berakhir.")
            return

        player_trophies.append(trophy)

    # Rentang trophy
    ranges = [
        (1, 100),
        (101, 500),
        (501, 1000),
    ]

    # Output pemain
    for i, trophy in enumerate(player_trophies, start=1):
        print(f"\nPemain {i}: Trophy = {trophy}")

    # Rekursif
    print("\nMusuh yang ditemukan (Rekursif):")
    start_time = time.time()
    enemies_recursive = find_enemies_recursive(player_trophies, ranges, num_enemies)
    recursive_time = time.time() - start_time
    for enemy in enemies_recursive:
        print(f"{enemy.name}: Trophy = {enemy.trophy}")
    print(f"Waktu eksekusi (Rekursif): {recursive_time:.6f} detik")

    # Iteratif
    print("\nMusuh yang ditemukan (Iteratif):")
    start_time = time.time()
    enemies_iterative = find_enemies_iterative(player_trophies, ranges, num_enemies)
    iterative_time = time.time() - start_time
    for enemy in enemies_iterative:
        print(f"{enemy.name}: Trophy = {enemy.trophy}")
    print(f"Waktu eksekusi (Iteratif): {iterative_time:.6f} detik")

if __name__ == "__main__":
    main()
