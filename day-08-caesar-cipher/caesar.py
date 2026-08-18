pesan = input("Masukkan pesan: ")

print("Pesan kamu:", pesan)

print(ord('A'))
print(ord('B'))

angka = ord('A')
angka_baru = angka + 1
huruf_baru = chr(angka_baru)
print(huruf_baru)



print(10 % 3)


print(26 % 26)
print(27 % 26)
print(28 % 26)

print(chr(ord('X') + 3))

posisi_X = ord('X') - ord('A')
print(posisi_X)


huruf = 'X'
geseran = 5

posisi = ord(huruf) - ord('A')
posisi_baru = (posisi + geseran) % 26
huruf_baru = chr(posisi_baru + ord('A'))

print(huruf_baru)