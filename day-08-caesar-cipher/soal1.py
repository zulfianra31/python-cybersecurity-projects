kata = "HELLO"      # kata yang mau dienkripsi
geseran = 5         # berapa posisi tiap huruf mau digeser
hasil = ""          # "wadah kosong" buat nampung hasil, diisi sedikit demi sedikit di dalam loop

for huruf in kata:
    # loop ini jalan sekali untuk TIAP huruf di dalam `kata`
    # contoh: putaran 1 → huruf = 'H', putaran 2 → huruf = 'E', dst

    posisi = ord(huruf) - ord('A')
    # ubah huruf jadi "posisi ke berapa di alfabet" (0-25)
    # kenapa dikurangi ord('A')? karena ord('A') mulai dari 65,
    # padahal kita mau posisi mulai dari 0 (A=0, B=1, dst)

    posisi_baru = (posisi + geseran) % 26
    # geser posisinya, lalu %26 supaya "muter balik" kalau kelewat Z

    huruf_baru = chr(posisi_baru + ord('A'))
    # ubah posisi (0-25) balik jadi huruf asli
    # ditambah ord('A') lagi supaya balik ke rentang kode ASCII huruf

    hasil = hasil + huruf_baru
    # ini bagian PENTING yang kemarin kelewat!
    # tanpa baris ini, huruf_baru cuma "numpang lewat" tiap putaran,
    # tidak pernah beneran disimpan

print(hasil)
# ini di LUAR loop (perhatikan tidak ada indentasi/spasi di depan)
# jadi baru jalan SETELAH semua huruf selesai diproses,
# nge-print hasil akhirnya yang sudah lengkap

kata = "HELLO WORLD"      
geseran = 5         
hasil = " "          

for huruf in kata:

    if huruf == ' ':
        hasil = hasil + huruf
    else:
        # kalau bukan spasi, jalankan proses geser seperti biasa
        posisi = ord(huruf) - ord('a')
        posisi_baru = (posisi + geseran) % 26
        huruf_baru = chr(posisi_baru + ord('a'))
        hasil = hasil + huruf_baru

print(hasil)

print('A'.isupper())
print('a'.isupper())
print('A'.islower())