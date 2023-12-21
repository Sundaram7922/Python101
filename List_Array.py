#Average or mean of a list

def average(l):
    sum = 0;
    for x in l:
        sum = sum + x
    n = len(l)
    return sum / n


z = [34, 56, 67, 43, 22]

print(average(z))


def mean(x):
    return sum(x) / len(x)


x = [34, 56, 67, 43, 22]
print(mean(x))


# Seperate Even or Odd

def even_odd(l):
    even = []
    odd = []
    for i in l:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)

    return even, odd


x = [34, 56, 67, 43, 22]
Even, Odd = even_odd(x)
print("Even :", Even)
print("Odd :", Odd)


# Get Smaller Element

def small(l, x):
    smaller = []
    for i in l:
        if i < x:
            smaller.append(i)

    return smaller


z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
x = 35

print("Smaller elements: ", small(z, x))

# List Comprehensions

z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
even = [x for x in l if x % 2 == 0]
odd = [x for x in l if x % 2 != 0]
print(even)
print(odd)

# String
l = ['geeks', 'sundaram', 'akshat', 'grammar', 'goat', 'ismart']
g_start = [i for i in l if i.startswith('g')]
print(g_start)

# sets

l = [10, 20, 3, 4, 10, 20, 7, 3]
s1 = {i for i in l if i % 2 == 0}
print(s1)

# Dictionary Comprehension

l = [1, 3, 4, 2, 5]
d1 = {x: x ** 3 for x in l}
print(d1)


# Larget element in list

def max_element(l):
    a = 0
    for i in l:
        if a < i:
            a = i
    return a


z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
print(max_element(z))


# Second largest element

def second_max(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None

    for i in l[1:]:
        if i > lar:
            slar = lar
            lar = i
        elif i != lar:
            if slar == None or slar < i:
                slar = i
    return slar


z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
print(second_max(z))


# Check if list is sorted or not

def issorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i - 1]:
            return False
        i = i + 1
    return True


z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
y = [10, 15, 20, 30]
print(issorted(y))


# Find the only odd

def find_odd(l):
    res = 0
    for i in l:
        res = res ^ i
    return res


l = [10, 20, 30, 10, 20]
print(find_odd(l))


# reverse a list

def rev(l):
    s = 0
    e = len(l) - 1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1


z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
rev(z)
print(z)


# Left rotate a list by one

def rotate(l):
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i - 1] = l[i]
    l[n - 1] = x


z = [34, 56, 67, 43, 22, 45, 23, 8, 7, 63, 20]
rotate(z)
print(z)
