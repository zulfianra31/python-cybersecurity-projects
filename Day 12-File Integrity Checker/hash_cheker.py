import hashlib

teks = "Hello World"
hasil_hash = hashlib.sha256(teks.encode())
print(hasil_hash.hexdigest())