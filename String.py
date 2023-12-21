### Reverse a string

def reverse(str):
    rev = " "
    for i in range(len(str)):
        rev += str[len(str) - i - 1]
    return rev


str = 'Geeks'
reverse(str)

s = 'Rascal'
s[::-1]

### String Comparison

print(ord('a'))
print(ord('z'))
print(chr(97))

'z' > 'a'

### Formated string in python

# 1. using %
name = "Samrat"
course = "python"

print("Welcome %s to %s" % (name, course))

# using format() function
print('welcome {0} to {1}'.format(name, course))

# Using f-string - Here we can use expression and function also
a = 10
b = 20
print(f"Welcome {name} to {course} and complete in {a + b} days")

### String Operation

# check for sub string

str1 = "geeksforgeeks"
str2 = 'geek'
str3 = 'gaak'
print(str2 in str1)
str3 in str2

# concatenation

str2 = 'geek'
str3 = 'gaak'
st = str2 + str3
st

# finding index
str1 = "geeksforgeeks"
str2 = 'geek'
print(str1.index(str2))
print(str1.rindex(str2))  # rindex give location from back

# operation
str1 = "geeksforgeeks"
print(len(str1))
print(str1.upper())
print(str1.islower())

print(str1.startswith('g'))
print(str1.endswith('geeks'))

str1 = "geeks for geeks"
print(str1.split())
l = ['geeks', 'for', 'geeks']
print(" ".join(l))
str1.strip(" ")  # remove white space

# find() - gives -1 if not present
str1 = "geeks for geeks"
print(str1.find('for'))
print(str1.find('loc'))


### Pattern Searching in python

def search(str1, str2):
    l = []
    for i in range(0, len(str1) - len(str2) + 1):
        if str1[i:len(str2) + i] == str2:
            l.append(i)
    return l


str1 = "geeks for geeks"
str2 = "geeks"
print(search(str1, str2))

str1 = "geeks for geeks data structre of python for geeks buddy"
str2 = "geeks"
pos = str1.find(str2)

while pos >= 0:
    print(pos)
    pos = str1.find(str2, pos + 1)


### Palindrome number

def palindrome(str):
    low = 0
    high = len(str) - 1
    while low < high:
        if str[low] != str[high]:
            return False
        low = low + 1
        high = high - 1

        return True


str = 'abcba'
palindrome(str)


### Anagram in python

def anagram(str1, str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    return s1 == s2


str1 = 'akshat'
str2 = 'hatask'

anagram(str1, str2)
