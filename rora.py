#Aurora Putri Novrizcha - 2605749
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
buah[3] = "DURIAN"

print(buah)

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
index = int(input("Masukkan index list: "))
new = input("Masukkan Nama Baru: ")
buah[index] = new
print(buah)

buah.sort()
print(buah)