# ===== KONSEP YANG DILATIH: Security Awareness & Python Fundamentals =====
# Program ini menilai seberapa kuat sebuah password berdasarkan 5 kriteria umum:
# panjang, huruf besar, huruf kecil, angka, dan simbol.
# Semakin banyak kriteria terpenuhi, semakin tinggi skornya.


def analisis_password(password):
    """
    Menganalisis sebuah password dan mengembalikan dictionary berisi
    detail tiap kriteria, skor total (0-5), dan label kekuatannya.
    """
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
            # bukan huruf dan bukan angka -> berarti simbol
            ada_simbol = True

    # True dihitung sebagai 1, False sebagai 0 -- jadi bisa langsung dijumlahkan
    skor = panjang_cukup + ada_huruf_besar + ada_huruf_kecil + ada_angka + ada_simbol

    if skor <= 2:
        label = "Lemah"
    elif skor <= 4:
        label = "Sedang"
    else:
        label = "Kuat"

    return {
        "panjang_cukup": panjang_cukup,
        "ada_huruf_besar": ada_huruf_besar,
        "ada_huruf_kecil": ada_huruf_kecil,
        "ada_angka": ada_angka,
        "ada_simbol": ada_simbol,
        "skor": skor,
        "label": label
    }


def tampilkan_hasil(hasil):
    """Menampilkan hasil analisis dengan format yang rapi dan mudah dibaca."""
    print()
    print("=== Hasil Analisis ===")
    print("Panjang minimal 8 karakter :", "✓" if hasil["panjang_cukup"] else "✗")
    print("Ada huruf besar            :", "✓" if hasil["ada_huruf_besar"] else "✗")
    print("Ada huruf kecil            :", "✓" if hasil["ada_huruf_kecil"] else "✗")
    print("Ada angka                  :", "✓" if hasil["ada_angka"] else "✗")
    print("Ada simbol                 :", "✓" if hasil["ada_simbol"] else "✗")
    print("Skor                       :", hasil["skor"], "/ 5")
    print("Kekuatan                   :", hasil["label"])
    print()


def main():
    print("=== Password Strength Analyzer ===")
    password = input("Masukkan password yang mau dicek: ")
    hasil = analisis_password(password)
    tampilkan_hasil(hasil)


if __name__ == "__main__":
    main()
