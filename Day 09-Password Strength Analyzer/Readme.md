# Day 09 — Password Strength Analyzer (Python)

Program yang menganalisis seberapa kuat sebuah password, berdasarkan 5 kriteria umum: panjang, huruf besar, huruf kecil, angka, dan simbol.

Ini versi Python dari konsep yang sama dengan Password Generator (Day 06, JavaScript) di seri sebelumnya — kali ini fokusnya kebalik: bukan membuat password, tapi menilai kekuatan password yang sudah ada.

## Konsep yang dilatih
- **Security awareness** — kriteria apa saja yang membuat password dianggap kuat/lemah, dasar penting sebelum masuk ke topik cybersecurity yang lebih dalam
- **Boolean sebagai "penanda"** — memakai variabel `True`/`False` untuk mencatat apakah suatu kondisi pernah terpenuhi selama loop berjalan
- **String method Python**: `.isupper()`, `.islower()`, `.isdigit()`, `.isalnum()`

## Fitur
- Mengecek 5 kriteria: panjang minimal 8 karakter, huruf besar, huruf kecil, angka, simbol
- Skor 0-5 berdasarkan jumlah kriteria yang terpenuhi
- Label kekuatan: Lemah / Sedang / Kuat
- Tampilan hasil yang rapi per kriteria (✓/✗)

## Cara Menjalankan
```
python password_checker.py
```

## Cara Kerja (ringkas)
1. Untuk tiap karakter dalam password, dicek apakah dia huruf besar, huruf kecil, angka, atau simbol — masing-masing dicatat dalam variabel boolean terpisah (`ada_huruf_besar`, dst)
2. Karena Python menghitung `True` sebagai `1` dan `False` sebagai `0`, kelima kriteria bisa langsung **dijumlahkan** untuk mendapat skor total, tanpa perlu banyak `if` bertingkat
3. Skor dipetakan ke label: 0-2 = Lemah, 3-4 = Sedang, 5 = Kuat

## Menemukan Fakta Menarik: `.isalnum()` untuk Deteksi Simbol
Python tidak punya fungsi bawaan `.issymbol()`. Solusinya: `.isalnum()` mengecek "apakah karakter ini huruf ATAU angka" — jadi untuk mendeteksi simbol, cukup pakai kebalikannya: `not karakter.isalnum()`. Kalau hasilnya `True`, berarti karakter itu bukan huruf dan bukan angka, alias simbol.

## Bonus: 2 Konsep Baru di Versi Final (belum dibahas sebelumnya)
Dua hal ini saya tambahkan di versi rapi ini, boleh dipelajari belakangan kalau belum familiar:
- **Dictionary** (`{"key": value, ...}`) — dipakai di `analisis_password()` untuk mengelompokkan banyak hasil (5 kriteria + skor + label) jadi 1 objek yang mudah dibawa-bawa, mirip konsep *object* di JavaScript
- **Ekspresi kondisional singkat** (`"✓" if kondisi else "✗"`) — cara memilih 1 dari 2 nilai dalam 1 baris, tanpa perlu `if/else` 4 baris penuh

## Yang Saya Pelajari
- Python memperlakukan `True` sebagai `1` dan `False` sebagai `0` secara otomatis saat dijumlahkan — bisa dimanfaatkan untuk sistem skor sederhana tanpa banyak percabangan
- Membedakan beberapa method pengecekan karakter bawaan Python (`isalpha`, `isdigit`, `isalnum`, `isupper`, `islower`) dan tahu kapan masing-masing dipakai
- Cara memecah satu masalah besar ("apakah password ini kuat?") menjadi beberapa pengecekan kecil yang lebih sederhana, lalu digabungkan