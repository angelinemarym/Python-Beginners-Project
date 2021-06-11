import random

def tebak(x):
    angka_random = random.randint(1, x)
    tebak = 0
    while tebak != angka_random:
        tebak = int(input(f"Tebak angka antara 1 dan {x}: "))
        if tebak < angka_random:
            print("Coba lagi, tebakan terlalu rendah")
        elif tebak > angka_random:
            print("Coba lagi, tebakan terlalu tinggi")
    print(f"Selamat, Anda berhasil menebak angka {angka_random}!")

tebak(10)
