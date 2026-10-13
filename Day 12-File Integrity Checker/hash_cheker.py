import hashlib

def hitung_hash(path_file):
    with open(path_file, "rb") as file:
        isi = file.read()
    return hashlib.sha256(isi).hexdigest()

path = r"E:\all project\project 2 (cyber)\Day 12-File Integrity Checker\file.txt"

hash_awal = hitung_hash(path)
print("Hash awal:", hash_awal)

input("Sekarang ubah isi file.txt, save, lalu tekan Enter di sini...")

hash_baru = hitung_hash(path)
print("Hash baru:", hash_baru)

if hash_awal == hash_baru:
    print("Integritas file terjaga.")
else:
    print("Integritas file telah berubah.")