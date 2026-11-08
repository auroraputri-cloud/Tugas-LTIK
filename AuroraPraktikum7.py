#Aurora Putri Novrizcha - 2605749

#Studi Kasus 1
for i in range (1, 6):
    harga = 25000
    total = harga * i

print (f"Total Biaya Pembelian : Rp", total)

#Studi Kasus 2 
for i in range (1, 6):
    nilai = float(input(f"Masukkan Nilai Mahasiswa ke-{i}: "))
    total = nilai + i

    rata_rata = total/5 
print (f"Rata-rata Nilai Mahasiswa", rata_rata)

#Studi Kasus 3
total_genap = 0
for i in range(0, 21, 2):
    total_genap += i 

print(f"Jumlah Seluruh Bilangan Genap", total_genap)


#Studi Kasus 4 
lulus = 0 
for i in range(1, 6):
    nilai = float(input(f"Masukkan Nilai Mahasiswa ke-{i}: "))

    if (nilai >= min):
        min.append(nilai)
print (f"Total Mahasiswa yang lulus: ", nilai)