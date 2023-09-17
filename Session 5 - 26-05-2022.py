# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

# Arrays - Temporarily adding and removing items to an array
clothes_rack = []
clothes_rack.append("dress")
clothes_rack.append("trousers")
clothes_rack.append("socks")
clothes_rack.append("skirt")
clothes_rack.append("shirt")
print(clothes_rack)
print(clothes_rack[1:3])
print(clothes_rack[1:4])
clothes_rack.extend(["t-shirt", "shoes", "cap"])
print(clothes_rack)
clothes_rack.insert(4, "gloves")
print(clothes_rack)
clothes_rack.remove("shoes")
del clothes_rack[5]
print(clothes_rack)
last_item=clothes_rack.pop()
print(last_item)
print(clothes_rack)
if "dress" in clothes_rack:
    print("I have found my dress")
else:
        print("I can't find my dress")
print(clothes_rack.index("gloves"))
clothes_rack.sort()
print(clothes_rack)
clothes_rack.reverse()
print(clothes_rack)
for x in clothes_rack:
    print(x)

