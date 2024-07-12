person = {"name" : "Alex", "gender": "M", "age" : "32", "address": "Bialik 40/25 Ashkelon", "phone": "0545580431" }
key = input("What information do you want to know about this person?").lower()
resualt = person.get(key, "That information is not available")
print(resualt)