import socket

target = "127.0.0.1"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hasil = s.connect_ex((target, port))

print(hasil)
s.close()