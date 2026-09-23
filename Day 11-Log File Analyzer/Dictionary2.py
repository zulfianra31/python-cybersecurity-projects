# ===== BAGIAN 1: Baca file log =====

with open(r"E:\all project\project 2 (cyber)\Day 11-Log File Analyzer\sample.log", "r") as file:
    # open(..., "r") = buka file dalam mode "read" (baca saja)
    # "with ... as file" = cara aman buka file, otomatis nutup lagi setelah selesai
    baris_baris = file.readlines()
    # .readlines() mengubah isi file jadi LIST, satu item per baris
    # contoh: ['baris 1\n', 'baris 2\n', 'baris 3\n', ...]


# ===== BAGIAN 2: Siapkan "buku catatan" kosong =====

catatan = {}
# dictionary kosong, nantinya diisi begini: {"ip_tertentu": jumlah_gagal_login}
# contoh nanti: {"203.0.113.55": 8, "198.51.100.23": 2}


# ===== BAGIAN 3: Loop lewat SEMUA baris log, satu per satu =====

for baris in baris_baris:
    # tiap putaran, `baris` isinya 1 baris log, contoh:
    # "2026-09-08 08:14:22 LOGIN_FAILED user=admin ip=203.0.113.55\n"

    if "LOGIN_FAILED" in baris:
        # cuma proses baris yang MENGANDUNG kata "LOGIN_FAILED"
        # baris LOGIN_SUCCESS otomatis dilewati/diabaikan

        potongan = baris.split("ip=")
        # motong baris jadi 2 bagian, di titik tulisan "ip="
        # potongan[0] = "2026-09-08 08:14:22 LOGIN_FAILED user=admin "
        # potongan[1] = "203.0.113.55\n"   <- ini yang kita mau

        ip = potongan[1]
        # ambil cuma bagian KEDUA (index 1) = nomor IP-nya

        ip = ip.strip()
        # .strip() membuang spasi/newline (\n) yang nempel di awal-akhir teks
        # tanpa ini, "203.0.113.55\n" akan dianggap BEDA dari "203.0.113.55"

        # --- sekarang kita punya `ip` yang bersih, saatnya dihitung ---

        if ip in catatan:
            # CEK: apakah IP ini SUDAH PERNAH tercatat sebelumnya?
            catatan[ip] = catatan[ip] + 1
            # kalau SUDAH ada, ambil angka yang sudah tersimpan, tambah 1
        else:
            catatan[ip] = 1
            # kalau BELUM PERNAH ada, ini kemunculan pertama -> mulai dari 1
            # (tanpa if/else ini, Python akan ERROR "KeyError" kalau langsung
            #  coba +1 ke IP yang belum pernah tercatat)

# Setelah loop ini SELESAI (sudah memproses semua baris),
# `catatan` sudah lengkap berisi semua IP dan berapa kali masing-masing gagal login


# ===== BAGIAN 4: Lihat hasil mentahnya dulu =====

print(catatan)
# nge-print SELURUH dictionary sekaligus dalam 1 baris,
# format: {'ip1': angka1, 'ip2': angka2, ...}


# ===== BAGIAN 5: "Membongkar" dictionary jadi baris per baris =====

for a, b in catatan.items():
    # .items() itu cara "membongkar" dictionary jadi pasangan-pasangan
    # tiap putaran loop: `a` = 1 kunci (IP), `b` = 1 nilai (jumlah gagal login)
    # nama `a` dan `b` itu BEBAS, boleh diganti nama apa saja
    print("IP:", a, "-> Gagal login:", b)
    # ini cuma buat kita LIHAT isinya per baris, belum ada logika penilaian


# ===== BAGIAN 6: Inti dari program ini -- kasih penilaian =====

for ip, jumlah in catatan.items():
    # loop lagi lewat dictionary yang sama, kali ini pakai nama `ip` dan `jumlah`
    # (boleh dipakai ulang loop kedua kalinya, tidak masalah)

    if jumlah >= 5:
        # KALAU jumlah gagal login 5 kali atau lebih -> dianggap mencurigakan
        # (5 ini disebut "threshold"/ambang batas, angkanya bebas ditentukan)
        print("⚠️  MENCURIGAKAN:", ip, "-", jumlah, "kali gagal login")
    else:
        # KALAU kurang dari 5 -> dianggap wajar/normal
        print("Normal:", ip, "-", jumlah, "kali gagal login")