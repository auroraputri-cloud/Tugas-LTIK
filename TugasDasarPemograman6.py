# TUGAS 3
# Aurora Putri Novrizcha - 2605749

nama = input("Masukkan Nama Anda: ")
tugas = float(input("Masukkan nilai tugas Anda: "))
uts = float(input("Masukkan nilai UTS Anda: "))
uas = float(input("Masukkan nilai UAS Anda: "))
rataRata = (tugas + uts + uas) / 3

if (rataRata >= 70):
    if (tugas >= 60 and uts >= 60 and uas >= 60):
        print(f"{nama} Kamu LULUS tanpa remedial")
    else:
        print(f"{nama} kamu LULUS dengan remedial")
else:
    if (rataRata >= 50):
        print(f"{nama} kamu TIDAK LULUS, diperbolehkan remedial")
    else:
        print(f"{nama} kamu TIDAK LULUS dan tidak diperbolehkan remedial")