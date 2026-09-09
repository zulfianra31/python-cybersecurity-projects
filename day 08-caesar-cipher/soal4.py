def geser_teks(kata, geseran):
    hasil = ""
    for huruf in kata:
        if not huruf.isalpha():
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

# baru kode percobaan dekripsi diletakkan di bawah sini
pesan_asli = "Hello, World!"
terenkripsi = geser_teks(pesan_asli, 5)
print("Terenkripsi:", terenkripsi)

hasil_dekripsi_1 = geser_teks(terenkripsi, 21)
print("Dekripsi (pakai 21):", hasil_dekripsi_1)

hasil_dekripsi_2 = geser_teks(terenkripsi, -5)
print("Dekripsi (pakai -5):", hasil_dekripsi_2)