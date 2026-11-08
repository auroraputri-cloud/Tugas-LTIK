
# Quiz 1 - Perulangan list buah
buah = ["apel", "anggur", "mangga", "jeruk", "melon"]

for x in buah:
    print(x)


# Quiz 2 - Melewati angka 5
x = 0

while x < 10:
    x += 1

    if x == 5:
        continue

    print(x)


# Studi Kasus 1 - Kelipatan 5 menjadi pass
for i in range(1, 51):
    if i % 5 == 0:
        print("pass")
    else:
        print(i)


# Latihan 2 - Input nama hewan
n = int(input("Masukkan jumlah hewan yang akan diinput: "))

hewan = []

for i in range(n):
    nama = input(f"Masukkan nama hewan ke-{i + 1}: ")
    hewan.append(nama)

for i in range(n):
    print(f"Hewan ke-{i + 1} adalah {hewan[i]}")


# Latihan 3 - Bilangan genap dan ganjil
n = int(input("Masukkan jumlah bilangan: "))

for i in range(1, n + 1):
    bilangan = int(input(f"Bilangan ke-{i}: "))

    if bilangan % 2 == 0:
        print(f"Bilangan {bilangan} adalah genap")
    else:
        print(f"Bilangan {bilangan} adalah ganjil")


# Latihan 4 - Kelipatan 3 dan 5
for i in range(1, 81):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# Latihan 5 - Sistem login sederhana
usernameBenar = "dasproRPL"
passwordBenar = "RPLfire!123"

while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == usernameBenar and password == passwordBenar:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")
