# Find all the Prime Numbers less than or equal to a given Number !!!

def prime_ef(x: int) -> bool:
    if x ==1:
        return False
    i=2
    for i in range(i, x*x):
        if i < x:
            if x%i ==0:
                return False
    return True

def primes(n):
    for i in range(2, n+1):
        if prime_ef(i):
            print(i)

if __name__=="__main__":
    a=10
   # primes(a)




# Sieve of eratosthens algorithms

def sieve(n):
    if n <= 1:
        return

    is_prime = [True] * (n + 1)

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:  #
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            print(i, end=" ")

if __name__ == "__main__":
    n = 181
    #sieve(n)



def sieve(n):
    if n <= 1:
        return

    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if is_prime[i]:  #
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            print(i, end=" ")

if __name__ == "__main__":
    n = 181
    sieve(n)