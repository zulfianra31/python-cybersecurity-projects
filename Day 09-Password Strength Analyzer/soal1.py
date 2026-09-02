password = input("Masukkan password: ")

panjang_cukup = len(password) >= 8

ada_huruf_besar = False
ada_huruf_kecil = False
ada_angka = False

for karakter in password:
    if karakter.isupper():
        ada_huruf_besar = True
    if karakter.islower():
        ada_huruf_kecil = True
    if karakter.isdigit():
        ada_angka = True


print("Panjang cukup:", panjang_cukup)
print("Ada huruf besar:", ada_huruf_besar)
print("Ada huruf kecil:", ada_huruf_kecil)
print("Ada angka:", ada_angka)