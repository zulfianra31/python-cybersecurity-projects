# Day 11 — Log File Analyzer (Python)

Program yang membaca file log berisi catatan percobaan login, lalu otomatis mendeteksi IP mana yang gagal login berkali-kali — indikasi umum serangan **brute force** (mencoba menebak password berulang-ulang).

Ini project pertama di seri Python-cybersecurity yang masuk ranah **Blue Team / SOC (Security Operations Center)** — kebalikan dari Port Scanner (Day 10) yang lebih ke arah "mengecek/menyerang", di sini kita "bertahan/memantau".

## Konsep yang dilatih
- **Membaca file** (`open()`, `.readlines()`)
- **String processing**: `.split()`, `.strip()`, `in` untuk mencari substring
- **Dictionary** sebagai "penghitung" (counter)
- **Analisis pola sederhana** — dasar dari cara kerja SOC Analyst membaca log

## Cara Menjalankan
```
python log_analyzer.py
```
Lalu masukkan nama/path file log yang mau dianalisis (contoh: `sample.log`, file contoh yang disediakan).

## Alur Program, Dijelaskan Selangkah Demi Selangkah

Ini bagian paling penting dari README ini — dibuat detail supaya bisa dibaca ulang kapan pun lupa alurnya.

### 1. Membaca file jadi list per baris
```python
with open(path_file, "r") as file:
    return file.readlines()
```
- `open(path, "r")` membuka file dalam mode **read** (baca saja)
- `with ... as file:` adalah cara aman membuka file di Python — file otomatis "ditutup" lagi setelah selesai, tanpa perlu memanggil `.close()` manual
- `.readlines()` mengubah seluruh isi file jadi **list**, satu item per baris. Contoh: `['baris 1\n', 'baris 2\n', ...]`

### 2. Menyaring baris yang relevan saja
```python
for baris in baris_baris:
    if "LOGIN_FAILED" not in baris:
        continue
```
- `in` mengecek apakah suatu teks **mengandung** kata tertentu — mengembalikan `True`/`False`
- `continue` artinya "lewati sisa kode di bawah ini, lanjut ke putaran loop berikutnya". Di sini dipakai supaya baris yang bukan `LOGIN_FAILED` (misal `LOGIN_SUCCESS`) langsung dilewati tanpa perlu membungkus semua kode berikutnya dalam `if`

### 3. Mengambil IP dari baris teks
```python
ip = baris.split("ip=")[1].strip()
```
Ini 3 langkah digabung jadi 1 baris:
- `baris.split("ip=")` memotong baris jadi 2 bagian, di titik tulisan `"ip="`. Hasilnya list: `[bagian_sebelum, bagian_sesudah]`
- `[1]` mengambil bagian **kedua** dari list itu (index 1) — yaitu nomor IP-nya
- `.strip()` membuang spasi/newline (`\n`) yang nempel di awal-akhir teks. Ini penting karena tanpa `.strip()`, `"203.0.113.55\n"` akan dianggap **berbeda** dari `"203.0.113.55"` oleh Python, sehingga IP yang sama tidak akan terhitung sebagai IP yang sama

### 4. Menghitung kemunculan tiap IP pakai dictionary
```python
if ip in catatan:
    catatan[ip] = catatan[ip] + 1
else:
    catatan[ip] = 1
```
- `catatan` adalah dictionary kosong (`{}`) di awal, diisi sedikit demi sedikit selama loop berjalan
- Setiap IP baru yang belum pernah tercatat akan **error** (`KeyError`) kalau langsung ditambah tanpa dicek dulu — makanya wajib dicek `if ip in catatan` sebelum menambah nilainya
- Kalau IP sudah ada → tambah nilainya 1. Kalau belum ada → mulai dari 1

### 5. Mengurutkan dan menampilkan hasil
```python
urutan = sorted(catatan.items(), key=lambda pasangan: pasangan[1], reverse=True)
```
- `.items()` "membongkar" dictionary jadi pasangan-pasangan `(ip, jumlah)` yang bisa di-loop
- `sorted(..., key=..., reverse=True)` mengurutkan pasangan-pasangan itu dari jumlah **terbesar ke terkecil**, supaya IP paling mencurigakan muncul paling atas di laporan
- Ini bagian paling rumit sintaksnya (`lambda`) — untuk sekarang cukup tahu efeknya (mengurutkan berdasarkan jumlah), tidak perlu paham detail `lambda` dulu; ini konsep lanjutan yang bisa dipelajari belakangan

### 6. Menentukan ambang batas "mencurigakan"
```python
if jumlah >= BATAS_MENCURIGAKAN:
    print("⚠️  MENCURIGAKAN ...")
else:
    print("Normal ...")
```
`BATAS_MENCURIGAKAN = 5` didefinisikan di paling atas file, mudah diubah tanpa perlu mengubah logika lainnya. Di dunia nyata, angka ambang batas seperti ini biasanya ditentukan oleh tim keamanan berdasarkan pola normal organisasi masing-masing (bukan angka baku universal).

## Kenapa Ini Penting di Dunia Nyata

SOC Analyst sungguhan menghadapi log dengan **ribuan hingga jutaan baris per hari** — mustahil dibaca manual satu-satu. Prinsip yang dilatih di project kecil ini (baca log → filter kejadian relevan → hitung pola per sumber → tandai yang melewati ambang batas) adalah **fondasi dasar** dari tools keamanan yang jauh lebih kompleks seperti SIEM (Security Information and Event Management).

## Bug/Kendala yang Ditemukan Selama Proses Belajar
- `\n` yang nempel di akhir tiap baris hasil `.readlines()` membuat IP yang sama dianggap berbeda kalau tidak dibersihkan pakai `.strip()`
- Mencoba menambah nilai ke dictionary untuk kunci yang belum pernah ada akan menghasilkan `KeyError` — harus dicek dengan `in` terlebih dahulu
- Membedakan `print(dictionary)` (menampilkan seluruh isi sekaligus) dengan `for key, value in dictionary.items()` (membongkar isi satu per satu untuk diproses)

## Yang Saya Pelajari
- Cara membaca file teks dan memprosesnya baris per baris
- Dictionary sebagai struktur data yang sangat berguna untuk "menghitung kemunculan sesuatu" — pola ini akan sering muncul lagi di banyak masalah pemrograman lain
- Pentingnya membersihkan data (whitespace, newline) sebelum diproses atau dibandingkan
- Cara berpikir seorang SOC Analyst: mengubah data mentah yang banyak menjadi kesimpulan yang jelas dan actionable ("IP ini mencurigakan, IP itu tidak")
