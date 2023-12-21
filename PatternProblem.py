# First Pattern

#n = int(input())
n = 5
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end='')
        j = j + 1
    print()
    i = i + 1

#Square Pattern 1

# n = int(input())
n = 5
i = 1
while (i <= n):
    j = 1
    while (j <= n):
        print(i, end='')
        j = j + 1
    print()
    i = i + 1

# Square Pattern 2

# n = int(input())
n = 5
i = 1
while (i <= n):
    j = 1
    while (j <= n):
        print(j, end='')
        j = j + 1
    print()
    i = i + 1

# Square Pattern 3

# n = int(input())
n = 5
i = 1
while (i <= n):
    j = n
    while (j != 0):
        print(j, end='')
        j = j - 1
    print()
    i = i + 1

# Traingular Pattern 1

#n = int(input())
n = 5
i = 1
while (i <= n):
    j = 1
    while (j <= i):
        print(j, end=' ')
        j = j + 1
    print()
    i = i + 1

# Traingular Pattern 2

#n = int(input())
n = 5
i = 1
while (i <= n):
    j = 1
    while (j <= i):
        print(j + i - 1, end=' ')
        j = j + 1
    print()
    i = i + 1

# Traingular Pattern 3

# n = int(input())
n = 5
i = 1
while (i <= n):
    j = 1
    while (j <= i):
        print(j + i - 1, end=' ')
        j = j + 1
    print()
    i = i + 1
