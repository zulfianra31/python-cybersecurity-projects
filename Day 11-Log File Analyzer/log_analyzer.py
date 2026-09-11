with open(r"E:\all project\project 2 (cyber)\Day 11-Log File Analyzer\sample.log", "r") as file:
    baris_baris = file.readlines()

print(len(baris_baris))
print(baris_baris[0])
print(baris_baris[1])

kalimat = "LOGIN_FAILED user=admin ip=203.0.113.55"
print("LOGIN_FAILED" in kalimat)
print("LOGIN_SUCCESS" in kalimat)