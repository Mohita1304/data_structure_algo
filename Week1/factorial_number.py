# Problem 1: We are given a number. The task is to find the factorial of the number.

# Approach 1: Iterative approach
def factorial(x):
    num=1
    for i in range(2, x+1):
        num=i * num
    return num

if __name__ == "__main__":
    number=6
    print(factorial(number))

# Approach 2: Recursive approach # Here assumption is n >=0.

def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    number = 6
    print(fact(number))


# Problem 2: We are given a number. The task is to find the Number of Trailing Zeros in the factorial of the number.
# The Trailing Zeros are the Zeros, which appear at the end of a number(factorial in that case)

# Naive approach

def trailing_zero(x):
    fact=1
    for i in range(2, x+1):
        fact= fact*i
    t_zero = 0
    while (fact % 10 ==0):
        t_zero=t_zero+1
        fact=fact // 10
    return t_zero

if __name__=='__main__':
    number=5
    print(trailing_zero(number))



# Efficient Approach

def e_trailing_zero(x):
    count=0
    i=5
    while (i<=x):
        count+=  x // i
        i = i * 5
    return count

if __name__== '__main__':
    number=251
    print(e_trailing_zero(number))