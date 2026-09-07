import socket

target = "127.0.0.1"
port = 445  # port yang biasanya dipakai Windows (file sharing)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hasil = s.connect_ex((target, port))

print(hasil)
s.close()

for angka in range(1, 5):
    print(angka)