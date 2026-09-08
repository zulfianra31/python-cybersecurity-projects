# ===== KONSEP YANG DILATIH: Networking Dasar =====
#
# ============================================================
# PERINGATAN ETIKA -- BACA SEBELUM PAKAI
# ============================================================
# Port scanning HANYA boleh dilakukan pada:
#   - localhost / 127.0.0.1 (komputer sendiri)
#   - Server/IP milik sendiri
#   - Target yang memang disediakan untuk latihan (misal scanme.nmap.org)
#
# JANGAN PERNAH scan IP/domain milik orang lain tanpa izin tertulis.
# Melakukannya tanpa izin bisa dianggap tindak pidana di banyak negara
# (termasuk Indonesia, di bawah UU ITE), meskipun "cuma iseng coba-coba".
# ============================================================

import socket

# Beberapa port umum dan layanan yang biasanya jalan di situ,
# supaya hasil scan lebih mudah dipahami (bukan cuma angka doang)
NAMA_LAYANAN = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC (Windows)",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB (File Sharing)",
    3306: "MySQL",
    3389: "RDP (Remote Desktop)",
    8080: "HTTP Alternatif"
}


def cek_port(target, port, timeout=0.5):
    """
    Mencoba konek ke satu port tertentu.
    Mengembalikan True kalau port terbuka, False kalau tertutup.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    hasil = s.connect_ex((target, port))
    s.close()
    return hasil == 0


def scan_range(target, port_awal, port_akhir):
    """
    Scan semua port dari port_awal sampai port_akhir (inklusif).
    Mengembalikan list berisi semua port yang terbuka.
    """
    port_terbuka = []

    print("Memindai", target, "dari port", port_awal, "sampai", port_akhir)
    print("(Proses ini bisa memakan waktu beberapa detik hingga menit)")
    print()

    for port in range(port_awal, port_akhir + 1):
        if port % 100 == 0:
            print("... sedang memeriksa port", port)

        if cek_port(target, port):
            nama = NAMA_LAYANAN.get(port, "Tidak diketahui")
            print("Port", port, "TERBUKA", "-", nama)
            port_terbuka.append(port)

    return port_terbuka


def main():
    print("=== Port Scanner Sederhana ===")
    print("PERINGATAN: hanya scan localhost atau server milik sendiri!")
    print()

    target = input("Masukkan target (kosongkan untuk localhost): ").strip()
    if target == "":
        target = "127.0.0.1"

    port_awal = int(input("Port awal (misal 1): ") or "1")
    port_akhir = int(input("Port akhir (misal 1024): ") or "1024")

    hasil = scan_range(target, port_awal, port_akhir)

    print()
    print("=== Selesai ===")
    if hasil:
        print("Total port terbuka ditemukan:", len(hasil))
        print("Daftar:", hasil)
    else:
        print("Tidak ada port terbuka ditemukan pada rentang ini.")


if __name__ == "__main__":
    main()
