password = input("Masukkan password: ")

panjang_cukup = len(password) >= 8

ada_huruf_besar = False
ada_huruf_kecil = False
ada_angka = False
ada_simbol = False

for karakter in password:
    if karakter.isupper():
        ada_huruf_besar = True
    if karakter.islower():
        ada_huruf_kecil = True
    if karakter.isdigit():
        ada_angka = True
    if not karakter.isalnum():
        ada_simbol = True

print("Panjang cukup:", panjang_cukup)
print("Ada huruf besar:", ada_huruf_besar)
print("Ada huruf kecil:", ada_huruf_kecil)
print("Ada angka:", ada_angka)
print("Ada simbol:", ada_simbol)

print(True + True)
print(True + False)
print(False + False)

skor = panjang_cukup + ada_huruf_besar + ada_huruf_kecil + ada_angka + ada_simbol
print("Skor:", skor)

if skor <= 2:
    label = "Lemah"
elif skor <= 4:
    label = "Sedang"
else:
    label = "Kuat"

print("Kekuatan password:", label)