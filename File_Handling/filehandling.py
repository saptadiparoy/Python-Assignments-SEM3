"""Create a Python script to read data from an input file. Perform line counting,
extract the first two lines, and write the extracted data into a new file."""

f1 = open ("Trial.txt", "r")

count= 0
data = f1.read()
words = data.split()

count =+ len(words)
print ("total words :", count)

lines = (f1.readlines())

sliced = lines [:2]
for i in sliced:
    print (i)

f1.close()

f2 = open("File2.txt", "w")
f2.writelines(sliced)
 
print ("File 2 made and updated succefully.")