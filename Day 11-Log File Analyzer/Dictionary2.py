with open(r"E:\all project\project 2 (cyber)\Day 11-Log File Analyzer\sample.log", "r") as file:
    baris_baris = file.readlines()

catatan = {}

for baris in baris_baris:
    if "LOGIN_FAILED" in baris:
        potongan = baris.split("ip=")
        ip = potongan[1]
        ip = ip.strip()

        if ip in catatan:
            catatan[ip] = catatan[ip] + 1
        else:
            catatan[ip] = 1

print(catatan)

for a, b in catatan.items():
    print("IP:", a, "-> Gagal login:", b)