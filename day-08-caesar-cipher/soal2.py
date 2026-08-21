kata = "Hello World"      
geseran = 5         
hasil = " "          

for huruf in kata:

    if huruf == ' ':
        hasil = hasil + huruf

    else if posisi = ord(huruf) - ord('a'):
        
        posisi_baru = (posisi + geseran) % 26
        huruf_baru = chr(posisi_baru + ord('a'))
        hasil = hasil + huruf_baru

    else:
        # kalau bukan spasi, jalankan proses geser seperti biasa
        posisi = ord(huruf) - ord('a')
        posisi_baru = (posisi + geseran) % 26
        huruf_baru = chr(posisi_baru + ord('a'))
        hasil = hasil + huruf_baru

print(hasil)