# ===== KONSEP YANG DILATIH: Blue Team / SOC -- Analisis Log =====
# Program ini membaca file log berisi catatan login, lalu mendeteksi
# IP mana saja yang gagal login berkali-kali (indikasi serangan brute force).

BATAS_MENCURIGAKAN = 5  # kalau gagal login >= angka ini, dianggap mencurigakan


def baca_log(path_file):
    """Membaca file log, mengembalikan list berisi tiap barisnya."""
    with open(path_file, "r") as file:
        return file.readlines()


def hitung_gagal_login_per_ip(baris_baris):
    """
    Menerima list baris log, mengembalikan dictionary
    berisi {ip: jumlah_gagal_login} untuk setiap IP yang pernah gagal login.
    """
    catatan = {}

    for baris in baris_baris:
        if "LOGIN_FAILED" not in baris:
            continue  # lewati baris ini, lanjut ke baris berikutnya

        ip = baris.split("ip=")[1].strip()

        if ip in catatan:
            catatan[ip] = catatan[ip] + 1
        else:
            catatan[ip] = 1

    return catatan


def tampilkan_laporan(catatan):
    """Menampilkan hasil analisis, IP mencurigakan ditandai jelas."""
    print()
    print("=== Laporan Analisis Login Gagal ===")

    if not catatan:
        print("Tidak ada aktivitas LOGIN_FAILED ditemukan di log ini.")
        return

    # urutkan dari yang paling sering gagal login, biar yang paling
    # mencurigakan muncul duluan di laporan
    urutan = sorted(catatan.items(), key=lambda pasangan: pasangan[1], reverse=True)

    for ip, jumlah in urutan:
        if jumlah >= BATAS_MENCURIGAKAN:
            print(f"⚠️  MENCURIGAKAN  | {ip:<16} | {jumlah} kali gagal login")
        else:
            print(f"   Normal        | {ip:<16} | {jumlah} kali gagal login")

    print()
    total_mencurigakan = sum(1 for jumlah in catatan.values() if jumlah >= BATAS_MENCURIGAKAN)
    print("Total IP mencurigakan:", total_mencurigakan, "dari", len(catatan), "IP yang pernah gagal login")


def main():
    print("=== Log File Analyzer ===")
    path_file = input("Masukkan path file log (contoh: sample.log): ").strip()

    baris_baris = baca_log(path_file)
    catatan = hitung_gagal_login_per_ip(baris_baris)
    tampilkan_laporan(catatan)


if __name__ == "__main__":
    main()
