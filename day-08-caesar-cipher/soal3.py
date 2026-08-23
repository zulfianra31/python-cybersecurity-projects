kata = "Hello World"      
geseran = 5         
hasil = ""

def geser_teks(kata, geseran):
    hasil = ""
    for huruf in kata:
        if huruf == ' ':
            hasil = hasil + huruf
        elif huruf.islower():
            posisi = ord(huruf) - ord('a')
            posisi_baru = (posisi + geseran) % 26
            huruf_baru = chr(posisi_baru + ord('a'))
            hasil = hasil + huruf_baru
        else:
            posisi = ord(huruf) - ord('A')
            posisi_baru = (posisi + geseran) % 26
            huruf_baru = chr(posisi_baru + ord('A'))
            hasil = hasil + huruf_baru
    return hasil

# cara manggilnya:
pesan_asli = input("Masukkan pesan: ")
pesan_terenkripsi = geser_teks(pesan_asli, 5)
print(pesan_terenkripsi)