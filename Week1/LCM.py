# Find out the LCM of two given number
from PIL.ImImagePlugin import number

from Week1.gcd_hcf import gcd_opt


def LCM(a,b):
    res = max(a,b)
    while True:
        if (res % a ==0 and res % b==0):
            return res
        res =res +1


if __name__=='__main__':
    a=8
    b=6
    print(LCM(a,b))


# Efficient approach

def gcd_ef(a,b):
    if b==0:
        return a
    else:
        return gcd_ef(b, a%b)

def LCM_ef(a,b):
    return a*b//gcd_opt(a,b)

if __name__=='__main__':
    a=14
    b=6
    print(LCM_ef(a,b))