# We are given two numbers. The task is to find the GCD / HCF of the numbers.
from PIL.ImImagePlugin import number
from numpy.testing.print_coercion_tables import print_new_cast_table


# GCF

def gcd(a,b):
    ret= min(a,b)
    while (ret >0):
        if  a % ret == 0 and b % ret == 0:
            break
        ret -= 1
    return ret

if __name__=='__main__':
    a = 15
    b= 20
   # print(gcd(a,b))


# Euclidean distance approach

def gcd_ed(a, b):
    while (a != b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if __name__ == '__main__':
    c = 12  # First number
    d = 15  # Second number
    #print(gcd_ed(c, d))  # Print the GCD of 12 and 15


#optimised  OptEuclidean distance approach

def gcd_opt(a,b):
    if b==0:
        return a
    else:
        return gcd_opt(b, a % b)

if __name__=="__main__":
    a=72
    b=64
    print(gcd_opt(a,b))