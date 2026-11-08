# LATIHAN 1-soal1
# Aurora Putri Novrizcha
# 2605749 - 1C

def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

jumlah = int(input("Masukkan banyak deret Fibonacci: "))
fibonacci(jumlah)

# LATIHAN 1-soal 2
# Aurora Putri Novrizcha
# 2605749 - 1C

def volumeTabung(r, t):
    return 22/7 * r * r * t

r = float(input("Masukkan jari-jari: "))
t = float(input("Masukkan tinggi: "))

hasil = volumeTabung(r, t)
print(f"Volume Tabung: ", hasil)

# LATIHAN 1 - soal 3
# Aurora Putri Novrizcha
# 2605749 - 1C

def hitungNilai(*args):
    total = sum(args)
    jumlah = len(args)

    if jumlah > 0:
        rataRata = total / jumlah
    else:
        rataRata = 0

    return total, rataRata

angka = input("Masukkan angka dipisahkan dengan koma: ")
data = [float(x.strip()) for x in angka.split(",")]

total, rataRata = hitungNilai(*data)

print("Total = ", total)
print("Rata-rata = ", rataRata)

# LATIHAN 2
# Aurora Putri Novrizcha
# 2605749 - 1C

def login():
    password_benar = "Latihan"
    kesempatan = 3

    while kesempatan > 0:
        password = input("Masukkan password: ")

        if password == password_benar:
            print("Login berhasil!")
            return
        else:
            kesempatan -= 1
            print("Password salah!")
            print("Sisa kesempatan:", kesempatan)

    print("Kesempatan habis. Anda keluar dari menu login.")

login()

# LATIHAN 3
# Aurora Putri Novrizcha
# 2605749 - 1C

# Latihan 3 
def selisihWaktu(mulai, selesai):
    return selesai - mulai

jam1 = int(input("Jam mulai: "))
menit1 = int(input("Menit mulai: "))
detik1 = int(input("Detik mulai: "))

jam2 = int(input("Jam selesai: "))
menit2 = int(input("Menit selesai: "))
detik2 = int(input("Detik selesai: "))

mulai = jam1 * 3600 + menit1 * 60 + detik1
selesai = jam2 * 3600 + menit2 * 60 + detik2

selisih = selisihWaktu(mulai, selesai)

print("Output:", selisih // 3600, "jam -",
      selisih % 3600 // 60, "menit -",
      selisih % 60, "detik")