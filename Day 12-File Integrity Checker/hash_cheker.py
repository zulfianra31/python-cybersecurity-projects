import hashlib

teks = "Hello World!"

with open(r"E:\all project\project 2 (cyber)\Day 12-File Integrity Checker\file.txt", "rb") as file:
    isi = file.read()

hasil_hash = hashlib.sha256(isi)
print(hasil_hash.hexdigest())