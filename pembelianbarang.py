print("=== PROGRAM KASIR SEDERHANA ===")

barang = input("Masukkan nama barang: ")
harga_satuan = int(input("Masukkan harga satuan: Rp"))
banyak = int(input("Masukkan jumlah pembelian: "))

subtotal = harga_satuan * banyak

if subtotal >= 100000:
    potongan = subtotal * 10 / 100
    keterangan = "Mendapat diskon 10%"
else:
    potongan = 0
    keterangan = "Tidak mendapat diskon"

total_bayar = subtotal - potongan

print("\n=== DETAIL PEMBELIAN ===")
print("Barang        :", barang)
print("Harga satuan  : Rp", harga_satuan)
print("Jumlah        :", banyak)
print("Subtotal      : Rp", subtotal)
print("Diskon        : Rp", potongan)
print("Keterangan    :", keterangan)
print("Total bayar   : Rp", total_bayar)
print("========================")