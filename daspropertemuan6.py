# TUGAS 1
# Aurora Putri Novrizcha - 2605749

nilai = float(input("Masukkan nilai Anda: "))

if (nilai >= 90):
    print("Nilai Anda A")
elif (nilai >= 80 ):
    print("Nilai Anda B")
elif (nilai >= 70):
    print("Nilai Anda C")
elif (nilai >= 70):
    print("Nilai Anda D")    

# TUGAS 2
# Aurora Putri Novrizcha - 2605749
    
gender = input("Gender Anda (Contoh: Pria/Wanita): ")
umur = int(input("Umur Anda saat ini: "))
tinggi = float(input("Tingga badan Anda (cm): "))
iq = int(input("Masukkan IQ Anda: "))

if (gender == "Wanita"):
    tinggiMin = 170
elif (gender == "Pria"):
    tinggiMin = 175
else:
    tinggiMin = None

if tinggiMin is None:
    print("Gender tidak valid")
elif (18 <= umur <= 25 and tinggi >= tinggiMin and iq >= 130):
    print("Berpotensi menjadi model catwalk")
else:
    print("Belum memenuhi persyaratan menjadi model catwalk")

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