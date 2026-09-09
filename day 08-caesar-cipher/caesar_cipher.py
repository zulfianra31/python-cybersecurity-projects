# ===== KONSEP YANG DILATIH: Kriptografi Dasar & Python Fundamentals =====
# Caesar Cipher adalah teknik enkripsi paling sederhana dalam sejarah kriptografi:
# tiap huruf digeser sejumlah posisi tertentu di alfabet.
# Contoh: geser 3 posisi -> A jadi D, B jadi E, dst (dan muter balik dari Z ke A lagi)


def geser_teks(kata, geseran):
    """
    Menggeser tiap huruf dalam `kata` sejauh `geseran` posisi di alfabet.
    Dipakai untuk ENCODE (geseran positif) maupun DECODE (geseran negatif,
    atau geseran positif yang totalnya 26 dengan geseran encode -- efeknya sama
    karena alfabet "muter balik" tiap 26 huruf).

    Karakter selain huruf (spasi, tanda baca, angka) dibiarkan apa adanya,
    tidak ikut digeser.
    """
    hasil = ""

    for huruf in kata:
        if not huruf.isalpha():
            # bukan huruf sama sekali (spasi, koma, tanda seru, angka, dll)
            # dibiarkan apa adanya, tidak ikut digeser
            hasil = hasil + huruf

        elif huruf.islower():
            # huruf kecil (a-z)
            posisi = ord(huruf) - ord('a')          # ubah jadi posisi 0-25
            posisi_baru = (posisi + geseran) % 26   # geser, %26 supaya muter balik
            huruf_baru = chr(posisi_baru + ord('a'))  # balik jadi huruf kecil
            hasil = hasil + huruf_baru

        else:
            # huruf besar (A-Z) -- logikanya sama, basisnya ord('A')
            posisi = ord(huruf) - ord('A')
            posisi_baru = (posisi + geseran) % 26
            huruf_baru = chr(posisi_baru + ord('A'))
            hasil = hasil + huruf_baru

    return hasil


def main():
    print("=== Caesar Cipher ===")
    print("1. Encode (enkripsi pesan)")
    print("2. Decode (dekripsi pesan)")
    pilihan = input("Pilih menu (1/2): ")

    pesan = input("Masukkan pesan: ")
    geseran = int(input("Masukkan jumlah geseran (misal 5): "))

    if pilihan == "1":
        hasil = geser_teks(pesan, geseran)
        print("Pesan terenkripsi:", hasil)
    elif pilihan == "2":
        # decode = encode dengan geseran negatif (arah mundur)
        hasil = geser_teks(pesan, -geseran)
        print("Pesan asli:", hasil)
    else:
        print("Pilihan tidak dikenali. Pilih 1 atau 2.")


# Baris ini memastikan main() hanya berjalan kalau file ini dijalankan langsung
# (bukan waktu di-import dari file lain -- ini praktik umum di Python)
if __name__ == "__main__":
    main()
