catatan = {}
catatan["203.0.113.55"] = 1
print(catatan)

catatan["203.0.113.55"] = catatan["203.0.113.55"] + 1
print(catatan)

# catatan = {}
# catatan["9.9.9.9"] = catatan["9.9.9.9"] + 1

catatan = {"203.0.113.55": 2}
print("203.0.113.55" in catatan)
print("9.9.9.9" in catatan)

catatan = {}
ip = "9.9.9.9"

# kemunculan IP yang PERTAMA
if ip in catatan:
    catatan[ip] = catatan[ip] + 1
else:
    catatan[ip] = 1

print(catatan)

# kemunculan IP yang KeDUA
if ip in catatan:
    catatan[ip] = catatan[ip] + 1
else:
    catatan[ip] = 1

print(catatan)