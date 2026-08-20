kata = "HELLO"
geseran = 5
hasil = ""


for huruf in kata:
    posisi = ord(huruf) - ord('A')
    posisi_baru = (posisi + geseran) % 26
    huruf_baru = chr(posisi_baru + ord('A'))


print(hasil)