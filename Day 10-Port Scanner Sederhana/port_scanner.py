import socket

target = "127.0.0.1"

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # <- baris baru: nunggu maksimal 0.5 detik per port
    hasil = s.connect_ex((target, port))
    
    if hasil == 0:
        print("Port", port, "TERBUKA")
    
    s.close()