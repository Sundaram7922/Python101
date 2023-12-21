
#Intro to Python

print('Hello World!')
a = 123
print("career", " All is well", sep=',')
print("Labs")
print(a)

# DATA TYPE

a = 10
print(type(a))
a = "Wow"
print(type(a))

# IF ELSE - Conditions
#n = int(input())
n = 32
if (n % 2 == 0):
    print("Even")
else:
    print("Odd")

# Using operators in if else
#a = int(input())
a = 23
#b = int(input())
b = 56
if (a > 10) and (b > 10):
    print("greater")
else:
    print("Less one")

# While loop

#n = int(input())
n = 10
count = 1
while (count <= n):
    print(count)
    count += 1

# FOR LOOP
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
   for y in fruits:
          print(x, y)


