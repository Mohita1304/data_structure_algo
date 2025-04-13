# print all the divisors of a given number.
from decorator import append


def divisor(n):
    for i in range(1, n+1):
        if n%i==0:
            print(i)

if __name__=="__main__":
    a=10
  #  divisor(a)


## Method 2

def divisor_eff(n):
    for i in range(1, int(n**0.5) + 1):
            if n%i==0:
                print(i)
                if i != (n/i):
                    print(n/i)

if __name__=="__main__":
    a=24
    #divisor_eff(a)


# in sorted way

def divisor_sort(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
            if n%i==0:
                print(i)
                if i != n/i:
                    factors.append(n/i)
    for factor in reversed(factors):
        print(factor)



if __name__=="__main__":
    a=10
    divisor_sort(a)