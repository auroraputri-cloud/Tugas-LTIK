barang = int(input("Masukkan jenis barang yang anda beli: "))
data = []

for i in range(barang):
    print(f"\nBarang ke-{i + 1}")

    nama = input("Nama barang: ")
    harga = int(input("Harga satuan: Rp"))
    jumlah = int(input("Jumlah beli: "))

    subtotal = harga * jumlah
    barang = {
        "nama": nama,
        "harga": harga,
        "jumlah": jumlah,
        "subtotal": subtotal
    }

    data.append(barang)

totalbelanja = 0

print("\nNama barang: ", barang["nama"])
print("\nharga: ", barang["harga"])
print("\njumlah: ", barang["jumlah"])
print("\nsubtotal: ", barang["subtotal"])

totalbelanja += barang["subtotal"]

if totalbelanja >= 200000:
    diskon = totalbelanja * 10/100
else:
    diskon = 0

totalbayar = totalbelanja - diskon

print("\n===== TOTAL PEMBAYARAN =====")
print("Total belanja : Rp", total_belanja)
print("Diskon        : Rp", int(diskon))
print("Total bayar   : Rp", int(total_bayar))

# list n tuple
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah[2] = "cherry"
nama = input("masukkan nama barang: ")
index = int(input("Masukkan index barang: "))

barang.insert(index, nama)
barang.sort()

print("daftar barang : ")
print(barang)