sudahInput = False
nama = nim = kelas = prodi = umur = telepon = ""

while True:
    print("\nMenu")
    print("1. Menginput biodata")
    print("2. Menampilkan biodata")
    print("3. Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        nama = input("Masukkan Nama Lengkap Anda: ")
        nim = input("Masukkan NIM Anda: ")
        kelas = input("Anda Berasal Dari Kelas: ")
        prodi = input("Masukkan Program Studi Anda: ")
        umur = input("Umur Anda Saat Ini: ")
        telepon = input("Masukkan Nomor Telepon Anda: ")
        sudahInput = True
        print("Biodata berhasil disimpan!")

    elif pilihan == "2":
        if sudahInput == True:
            print("Nama Lengkap :", nama)
            print("NIM:", nim)
            print("Kelas        :", kelas)
            print("Program Studi:", prodi)
            print("Umur         :", umur)
            print("Nomor Telepon:", telepon)
        else:
            print("Biodata Belum Diinput")

    elif pilihan == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid")