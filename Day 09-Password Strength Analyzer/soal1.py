password = input("Masukkan password: ")
panjang = len(password)

if panjang >= 8:
    print("Panjang: OK")
else:
    print("Panjang: Terlalu pendek")