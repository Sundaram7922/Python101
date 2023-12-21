# 1. Check Prime no.
def isprime(n):
    for i in range(2, n):
           if (n % i == 0):
                       break
           else:
              return True

    return False

print(isprime(7))




