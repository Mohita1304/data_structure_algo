# Given number is prine number or not
from PIL.ImImagePlugin import number
from sqlalchemy import false


def prime(x: int) -> bool:
    if x ==1:
        return False
    i=2
    for i in range(i, x+1):
        if i < x:
            if x%i ==0:
                return False
    return True


if __name__=='__main__':
    number=18
    #print(prime(number))


# Efficient method

def prime_ef(x: int) -> bool:
    if x ==1:
        return False
    i=2
    for i in range(i, x*x):
        if i < x:
            if x%i ==0:
                return False
    return True


if __name__=='__main__':
    number=199
    #print(prime_ef(number))


# Efficient method 2

def prime_ef2(x: int) -> bool:
    if x ==1:
        return False
    if x ==2 or x==3:
        return False
    i=5
    for i in range(i, x*x):
        if i < x:
            if x%i ==0 or x% (i+2)==0:
                return False
            i=i+6
    return True


if __name__=='__main__':
    number=1111
   # print(prime_ef2(number))



##   Find out the all prime factors of a given number.

def print_prime_factors(n):
    if n <= 1:
        return
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            print(i, end=" ")
            n //= i

    if n > 1:
        print(n, end=" ")

    print()

if __name__ == "__main__":
    n = 12
    print_prime_factors(n)  # Output: 2 3 3 5 5



#### Optimized efficient method

def print_prime_factors(n):
    if n <= 1:
        return

    while n % 2 == 0:
        print(2, end=" ")
        n //= 2

    while n % 3 == 0:
        print(3, end=" ")
        n //= 3


    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            print(i, end=" ")
            n //= i

        while n % (i + 2) == 0:
            print(i + 2, end=" ")
            n //= (i + 2)


    if n > 3:
        print(n, end=" ")

    print()

if __name__ == "__main__":
    n = 450
    print_prime_factors(n)



