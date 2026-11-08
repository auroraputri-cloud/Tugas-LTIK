kalimat = input("Masukkan sebuah kalimat: ")

while True:
    print("\nMenu Operasi")
    print("1. Hitung jumlah kata")
    print("2. Ubah ke huruf kapital semua")
    print("3. Balik urutan kata")
    print("4. Ganti kalimat")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    kata = kalimat.split()

    if pilihan == "1":
        print("Jumlah kata:", len(kata))

    elif pilihan == "2":
        print("Hasil:", kalimat.upper())

    elif pilihan == "3":
        kata.reverse()
        hasil = ""
        for k in kata:
            hasil = hasil + k + " "
        print("Hasil:", hasil)

    elif pilihan == "4":
        kalimat = input("Masukkan kalimat baru: ")
        print("Kalimat berhasil diganti!")

    elif pilihan == "5":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")