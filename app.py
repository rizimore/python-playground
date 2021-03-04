# variables

a = 1  # int
b = 2.235  # float
c = 3.3333333333333333333  # double
d = 'd'  # string
e = "elephant"  # string
f = False  # boolean
g = [a, b, c]  # list
h = None  # null
i = (a, b)  # pair
j = {a, b, c, d}  # set
k = {
    "a": a,
    "b": b
}  # dictionaries

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

print(type(a))
print(type(b))

if isinstance(a, int):
    print("int")
else:
    print("not int")

# Number Helper Methods
print(round(b, 2))

# String Helper Methods
str1 = "Hello"
str2 = "World"
str3 = "Python is awesome!"
tags = "html5, css3, javascript, php, mysql"

print(str1, str2)  # concatenation
print(len(str1), len(str2))  # length
print(str3.count("o"))  # count characters
print(str3.index("o"))  # check character index
print(str3[0:6])  # range operator
print(str3[7:])
print(str3[:6])
print(str3[-1])
print(str3[0:6:2])
print(str3[::-1])
print(str3.upper())
print(str3.lower())
print(str3.swapcase())
print(str3.startswith('P'))
print(tags.split(", "))
print("Hello, %s" % str2)
print(f"Hello, {str2}")

# List Helper Methods
names = ["Hassan", "Mubashir", "Habib"]
names.append("Rooma")
names.append("Saad")
del names[3]
names.pop(1)
names.remove("Habib")
names.reverse()

print(names)
print(names[1])
print(len(names))
print(names.count("Saad"))

# Operators
if "Saad" in names:
    print("True")

if (not f) is True:
    print("True")
else:
    print("False")


# Functions
def sum(num1, num2):
    return num1 + num2


print(sum(1, 2))


# Classes and Objects
class User:
    name = None

    def setName(self, user_name):
        self.name = user_name

    def getName(self):
        return self.name

mubashir = User()
mubashir.setName("Mubashir")
print(mubashir.getName())


# Loops
print(range(2, 5))
for i in range(2, 10, 2):
    print(i)

count = 0
while False:
    count += 1
    print(count)
    if count == 2:
        break
else:
    print("Sorry!")

for name in names:
    print(name)








