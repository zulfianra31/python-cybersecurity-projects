# Day 10 — Port Scanner Sederhana (Python)

Program yang memeriksa port mana saja yang terbuka pada sebuah alamat IP, dengan indikator progress dan identifikasi nama layanan umum.

⚠️ **Lihat bagian Peringatan Etika di bawah sebelum menjalankan program ini.**

## Konsep yang dilatih
- **Networking dasar** — apa itu port, cara komputer "mengetuk pintu" alamat dan port tertentu untuk mengecek ketersediaan layanan
- **Modul `socket`** — pustaka bawaan Python untuk komunikasi jaringan
- **Dictionary** — memetakan nomor port ke nama layanan yang biasa berjalan di situ

## ⚠️ Peringatan Etika
Port scanning **hanya boleh** dilakukan pada:
- `localhost` / `127.0.0.1` (komputer sendiri)
- Server/IP milik sendiri
- Target yang memang disediakan untuk latihan (misal `scanme.nmap.org`, situs resmi Nmap untuk latihan scanning)

**Jangan pernah** scan IP/domain milik orang lain tanpa izin tertulis. Melakukannya tanpa izin bisa dianggap tindak pidana di banyak negara (termasuk Indonesia, di bawah UU ITE), meskipun niatnya cuma coba-coba/belajar.

## Fitur
- Scan rentang port yang bisa diatur bebas (misal 1-1024)
- Indikator progress tiap 100 port, supaya tidak terlihat seperti macet saat scan rentang besar
- Identifikasi nama layanan umum untuk port yang ditemukan terbuka (misal port 445 → SMB/File Sharing)
- Timeout per port supaya scan tidak menggantung lama di port yang tidak merespons

## Cara Menjalankan
```
python port_scanner.py
```
Kosongkan target untuk otomatis scan `127.0.0.1` (localhost).

## Cara Kerja (ringkas)
1. Untuk tiap nomor port dalam rentang yang ditentukan, `socket.connect_ex((target, port))` dicoba
2. Hasilnya berupa angka: `0` berarti berhasil konek (port **terbuka**), selain `0` berarti gagal (port **tertutup**) — angka spesifiknya bisa beda tergantung sistem operasi, jadi yang dicek cuma "apakah `0` atau bukan"
3. `settimeout()` dipasang supaya program tidak menunggu terlalu lama untuk tiap port yang tidak merespons
4. Dictionary `NAMA_LAYANAN` dipakai untuk menerjemahkan nomor port ke nama layanan yang familiar, memakai method `.get(key, default)` — kalau port-nya tidak ada di dictionary, otomatis menampilkan "Tidak diketahui" alih-alih error

## Bug/Kendala yang Ditemukan Selama Proses Belajar
- Scan rentang besar (1-1024) tanpa `timeout` bisa terasa seperti "macet" karena tidak ada indikasi progress — solusinya: tambahkan `print` progress tiap kelipatan 100 port (`if port % 100 == 0`)
- `range(mulai, sampai)` di Python **tidak menyertakan** angka `sampai` — penting diperhatikan supaya port terakhir tidak terlewat saat scan

## Yang Saya Pelajari
- Cara kerja dasar koneksi TCP: mencoba membuka koneksi ke sebuah port untuk mengetahui apakah ada layanan yang mendengarkan di situ
- Pentingnya `timeout` dalam operasi jaringan, supaya program tidak menggantung tanpa batas waktu
- Dictionary sebagai cara memetakan satu nilai ke nilai lain (nomor port → nama layanan), dan method `.get()` untuk mengambil nilai dengan aman tanpa error kalau key-nya tidak ada
- Modulo (`%`) ternyata berguna bukan cuma untuk "muter balik" (seperti di Caesar Cipher), tapi juga untuk mengecek kelipatan angka tertentu (dipakai untuk indikator progress)
- Pentingnya kesadaran etika dan hukum sebelum menjalankan tools yang menyentuh ranah keamanan jaringan
