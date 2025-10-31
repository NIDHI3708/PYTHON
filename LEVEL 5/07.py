s = {}
a = input("Ritika's favourite language is: ")
s.update({"Ritika": a})
b = input("Ritika's favourite language is: ") #It will get updated
s.update({"Ritika": b})
c = input("Sonia's favourite language is: ")
s.update({"Sonia": c})
d = input("Neha's favourite language is: ")
s.update({"Neha": d})
print(s)