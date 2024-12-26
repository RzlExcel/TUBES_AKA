import random
import time

class Player:
    def __init__(self, name, trophy):
        self.name = name
        self.trophy = trophy

def find_enemies_recursive(player_trophies, ranges, num_enemies, index=0, enemy_index=1):
    if index >= len(player_trophies): 
        return []

    enemies = []
    trophy = player_trophies[index]

    for r in ranges:
        if r[0] <= trophy <= r[1]:
            for _ in range(num_enemies // len(player_trophies)):
                enemy_trophy = random.randint(r[0], r[1])
                enemies.append(Player(name=f"Enemy{enemy_index}", trophy=enemy_trophy))
                enemy_index += 1
            break

    return enemies + find_enemies_recursive(player_trophies, ranges, num_enemies, index + 1, enemy_index)

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
    random.seed()

    num_players = int(input("Masukkan jumlah pemain (1 atau 2): "))

    if num_players not in [1, 2]:
        print("Jumlah pemain harus 1 atau 2. Program akan berhenti.")
        return

    num_enemies = 8  
    if num_players == 1:
        num_enemies = 9  

    player_trophies = []
    for i in range(1, num_players + 1):
        trophy = int(input(f"Masukkan trophy untuk pemain {i}: "))

        if trophy > 1000:
            print("Trophy tidak boleh lebih dari 1000. Program berakhir.")
            return

        player_trophies.append(trophy)

    ranges = [
        (1, 100),
        (101, 500),
        (501, 1000),
    ]


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
