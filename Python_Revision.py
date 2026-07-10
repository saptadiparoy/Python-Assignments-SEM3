#to find area of a rectangle

def arearect(l , b):
    area = l * b
    print (f"area of rectangle is: {area}")

arearect(3,4)

#to check whether a number is even or odd
def evencheck(x):
    if x % 2 == 0:
        print ("Number is even.")

    else:
        print("Number is odd.")

evencheck(5)
evencheck(8)
#swapping numbers
x = 3
z = x
y = 4

x = y
y = z
print(x, y)

#to check whether a year is leap year
def leapcheck(year):
    if year % 4 == 0:
        print(f"The year {year} is a leap year.")

    else:
        print("Given year is not a leap year.")

leapcheck(2024)

#prog to check whteher a number is positive negative or zero

def numcheck(x):
    if x > 0:
        print ("Positive")

    elif x < 0:
        print ("Negative")

    else:
        print ("Zero")

numcheck(-9)

#to check a students grades accoridng to marks

def grades(t):
    if t > 90:
        print ("O")

    elif t > 70 and t < 80:
        print ("A")

    elif t > 60 and t < 70:
        print ("B")

    elif t > 50 and t < 60:
        print ("c")

    elif t > 40 and t < 50:
        print ("D")

    elif t < 40:
        print ("F")

    else:
        print("Invalid")


grades(75)

#to find factorial of a number
def factorial(i):
    fact = 1
    for x in range(1 , i+1):
        fact *= x
    print (f"Factorial is:   {fact}")

factorial(4)

#fibonacci sequence generator
def fibo (n):
    fiblist = [0,1]
    while len(fiblist) < n:
        fiblist.append(fiblist[-1] + fiblist [-2])
    print (fiblist)

fibo (10)

#function to reverse a string
def reversestring(x):
    print (f"Reversed string is :   {(x[::-1])}")

reversestring("hello")

#func to find sum of all numbers in a list
def sum_list(x):
    sum = 0
    for i in x:
        sum += i

    print ("Sum of all numbers in list: ", sum)

examplelist = [1,2,4,7]
sum_list(examplelist)


#to find the maximum out of three numbers:
def maxcheck(x,y,z):
    print(max(x,y,z))

maxcheck(0,10,400)


#merging two dictionaries (using update func):
d1 = {"x" : 1, "y" : 4}
d2 = {"z" : 9, "y" : 7, "g": 0}
d1.update(d2)
print(d1)

#to read contents of a file:
f = open("newtext.txt", "w")
f.write("NEW TEXT TO NEWTEXT FILE!! :D")

f.close
f = open("newtext.txt", "r")
conetnt = f.read()
print (conetnt)

#error handle wrong input
while True:
    try:
        num = int(input("Please enter a number:   "))
        print ("Entered number is:  ", num)
        break

    except Exception as e:
        print("Please enter valid NUMBER!")