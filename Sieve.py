
# Sieve of Eratosthenes

num  =int(input())


def isprime(num):
    i =2
    while i*i <=num:
        if num%i == 0:
            return False
        i+1
    return True

ans = isprime(num)
print (ans)   






num  =int(input())


def isprime(num):
    i =2
    while i*i <=num:
        if num%i == 0:
            return False
        i+1
    return True

ans = isprime(num)
print (ans)        