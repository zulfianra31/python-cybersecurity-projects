kata = "Hello World"   # kalimat yang mau dienkripsi (masih hardcode/tetap, belum bisa ganti-ganti)
geseran = 5             # jumlah pergeseran huruf di alfabet
hasil = ""              # wadah kosong buat nampung hasil, diisi sedikit demi sedikit di dalam loop
                        # PENTING: harus benar-benar kosong ("") bukan ada spasi (" "),
                        # supaya tidak ada karakter tambahan nyelip di depan hasil akhir

for huruf in kata:
    # loop ini jalan sekali untuk TIAP karakter di dalam `kata`,
    # termasuk spasi -- karena spasi juga dihitung 1 karakter

    if huruf == ' ':
        # KASUS 1: karakternya spasi
        # spasi tidak boleh ikut digeser (kalau ikut digeser, hasilnya jadi karakter aneh/sampah)
        # jadi cukup tambahkan spasi aslinya apa adanya ke `hasil`
        hasil = hasil + huruf

    elif huruf.islower():
        # KASUS 2: karakternya huruf KECIL (a-z)
        # .islower() otomatis ngecek True/False, tidak perlu ord() buat ngecek ini

        posisi = ord(huruf) - ord('a')
        # ubah huruf jadi "posisi ke berapa di alfabet" (0-25)
        # pakai ord('a') karena ini khusus huruf KECIL

        posisi_baru = (posisi + geseran) % 26
        # geser posisinya, %26 supaya "muter balik" kalau kelewat huruf 'z'

        huruf_baru = chr(posisi_baru + ord('a'))
        # ubah posisi (0-25) balik jadi huruf, tetap pakai ord('a')
        # supaya hasilnya tetap huruf KECIL (konsisten sama huruf aslinya)

        hasil = hasil + huruf_baru
        # tambahkan huruf yang sudah digeser ke `hasil`

    else:
        # KASUS 3: kalau bukan spasi dan bukan huruf kecil,
        # berarti pasti huruf BESAR (A-Z)
        # logikanya sama persis kayak KASUS 2, tapi basisnya ord('A') (huruf besar)

        posisi = ord(huruf) - ord('A')
        posisi_baru = (posisi + geseran) % 26
        huruf_baru = chr(posisi_baru + ord('A'))
        # pakai ord('A') di sini juga, supaya hasilnya tetap huruf BESAR

        hasil = hasil + huruf_baru

print(hasil)
# ini di LUAR loop (tidak ada indentasi di depan)
# jadi baru nge-print SETELAH semua huruf di `kata` selesai diproses satu-satu