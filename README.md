# Day 08 — Caesar Cipher (Python)

Program enkripsi & dekripsi teks pakai Caesar Cipher — teknik kriptografi paling sederhana dalam sejarah, di mana tiap huruf digeser sejumlah posisi tertentu di alfabet.

Ini project pertama dari seri belajar Python untuk cybersecurity, sekaligus project pertama saya di bahasa Python.

## Konsep yang dilatih
- **Kriptografi dasar** — cara kerja algoritma enkripsi paling klasik, dasar sebelum belajar algoritma yang lebih kompleks
- **Python fundamentals** — variabel, `for` loop, `if/elif/else`, function, dan operasi karakter (`ord()`, `chr()`)
- **Modulo (`%`)** — teknik "muter balik" angka, dipakai supaya pergeseran huruf tidak keluar dari batas alfabet (Z tidak lompat ke karakter aneh, tapi balik lagi ke A)

## Fitur
- Encode (enkripsi) dan decode (dekripsi) pesan
- Mendukung huruf besar dan kecil, dengan hasil yang konsisten (huruf besar tetap besar, kecil tetap kecil)
- Karakter non-huruf (spasi, tanda baca, angka) dibiarkan apa adanya, tidak ikut digeser
- Geseran bisa diatur bebas oleh pengguna

## Cara Menjalankan
```
python caesar_cipher.py
```
Lalu ikuti instruksi di layar: pilih encode/decode, masukkan pesan, masukkan jumlah geseran.

## Cara Kerja (ringkas)
1. Tiap karakter di pesan diperiksa: apakah dia huruf atau bukan?
2. Kalau bukan huruf (spasi, koma, dll), dibiarkan apa adanya
3. Kalau huruf, posisinya di alfabet dihitung (`ord(huruf) - ord('a')` untuk huruf kecil, atau `ord('A')` untuk huruf besar), digeser, lalu `%26` diterapkan supaya "muter balik" kalau melewati huruf terakhir alfabet
4. Posisi baru diubah kembali jadi huruf (`chr()`)
5. Decode ternyata **tidak butuh function terpisah** — cukup panggil function yang sama dengan geseran negatif (kebalikan arah), karena efek modulo membuat "maju 21" sama hasilnya dengan "mundur 5" untuk alfabet 26 huruf

## Bug yang Saya Temukan Sendiri Selama Proses Belajar (dan cara memperbaikinya)
Ini bagian yang paling banyak melatih pemahaman — bukan cuma nulis kode yang langsung benar:
- Lupa menyimpan hasil ke variabel `hasil` di dalam loop (huruf sudah dihitung, tapi tidak pernah "disimpan")
- Salah pakai `=` (assign) padahal butuh `==` (bandingkan) di dalam kondisi `if`
- Huruf besar dan kecil punya kode ASCII dasar yang beda (`ord('A')` = 65, `ord('a')` = 97), sehingga rumus geser harus disesuaikan tergantung jenis hurufnya
- Spasi dan tanda baca ikut "kena geser" kalau tidak ada pengecekan khusus (`isalpha()`) untuk mengecualikan karakter non-huruf
- Urutan pengecekan `if/elif/else` penting — kondisi yang terlalu umum diletakkan terlalu awal bisa "menangkap" kasus yang seharusnya ditangani kondisi lain di bawahnya
- Variabel yang dibuat di luar function tidak otomatis bisa diakses di dalam function (konsep *scope*)

## Yang Saya Pelajari
- Perbedaan sintaks Python dengan bahasa lain yang sudah saya kenal (JavaScript/C): pakai indentasi bukan kurung kurawal, `elif` bukan `else if`, tidak perlu semicolon
- `ord()` dan `chr()` sebagai jembatan antara representasi huruf dan angka
- Method bawaan string Python (`isalpha()`, `islower()`, `isupper()`) yang menggantikan pengecekan manual yang lebih ribet
- Konsep *scope*: variabel di dalam function itu terpisah dari variabel di luar, meski namanya sama
- Kenapa proses debugging (nemuin bug sendiri lewat eksperimen, bukan langsung dikasih kode benar) jauh lebih nempel di ingatan dibanding baca kode jadi