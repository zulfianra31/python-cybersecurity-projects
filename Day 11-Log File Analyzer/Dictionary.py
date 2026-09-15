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