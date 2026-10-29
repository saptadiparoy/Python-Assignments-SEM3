f1 = open ("Trial.txt", "r")
print ("Current pointer position: ", f1.tell())

print(f1.read())
print ("pointer position after reading file: ", f1.tell())

f1.seek(7)
print ("Pointer position after seek: ", f1.tell())