#perhitungan biaya konsumsi
jumlahPeserta = int(input("Masukkan Jumlah Peserta Seminar: "))
hargaPaket = 35000
cadangan = 0.10

jumlahCadangan = (jumlahPeserta) * (cadangan)
totalKonsumsi = jumlahPeserta + jumlahCadangan
totalBiayaKonsumsi = totalKonsumsi * hargaPaket

print("A. Perhitungan Biaya Konsumsi")
print(f"Jumlah Peserta: {jumlahPeserta} orang")
print(f"Jumlah cadangan (10%) dari Jumlah Peserta: {jumlahCadangan} orang")
print(f"Total Konsumsi yang harus disediakan: {totalKonsumsi}")
print(f"Total Biaya Konsumsi yang Perlu Disediakan: Rp{totalBiayaKonsumsi}")

#perhitungan kebutuhan cetak sertifikat
lembarPerRim = 500
hargaPerRim = 65000
cadangan = 0.05

jumlahCadanganSertifikat = (jumlahPeserta * cadangan)
jumlahSertifikat = jumlahPeserta * 1
jumlahKertas = int(jumlahSertifikat + jumlahCadanganSertifikat)
totalRim = float(jumlahKertas / lembarPerRim)

totalBiayaKertas = int(totalRim * hargaPerRim)

print("B. Perhitungan Kebutuhan Cetak Sertifikat")
print(f"Jumlah Sertifikat yang Perlu Dicetak: {jumlahSertifikat} lembar")
print(f"Jumlah Lembar Kertas yang Diperlukan: {jumlahKertas} lembar")
print(f"Total Rim Kertas yang Diperlukan: {totalRim} rim")
print(f"Total Biaya Pembelian Kertas: Rp{totalBiayaKertas}")

#perhitungan biaya pendaftaran peserta
biayaSewaTempat = int(input("Masukkan Biaya Sewa Tempat: "))
biayaDokumentasi = int(input("Masukkan Biaya Dokumentasi:"))
cadanganDana = 0.10

totalBiayaAcara = (totalBiayaKonsumsi + totalBiayaKertas + biayaSewaTempat + biayaDokumentasi)
danaCadangan = int(totalBiayaAcara * cadanganDana)
totalDanaDikumpulkan = int(totalBiayaAcara + danaCadangan)
biayaPendaftaranPeserta =int((totalDanaDikumpulkan + jumlahPeserta - 1) / jumlahPeserta)

print("C. Perhitungan Biaya Pendaftaran")
print(f"Total Biaya Penyelenggaraan Acara: Rp{totalBiayaAcara}")
print(f"Besar Dana Cadangan (10%): Rp{danaCadangan}")
print(f"Total Dana yang Harus Dikumpulkan: Rp{totalDanaDikumpulkan}")
print(f"Biaya Pendaftaran per Peserta: Rp{biayaPendaftaranPeserta}")