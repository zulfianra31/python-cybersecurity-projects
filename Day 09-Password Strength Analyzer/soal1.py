password = input("Masukkan password: ")
panjang = len(password)

if panjang >= 8:
    print("Panjang: OK")
else:
    print("Panjang: Terlalu pendek")


ada_huruf_besar = False   # penanda awal: belum ketemu

for karakter in password:
    if karakter.isupper():
        ada_huruf_besar = True   # begitu ketemu 1 aja, ubah jadi True

print(ada_huruf_besar)