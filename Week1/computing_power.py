# We are given two numbers. The task is to compute Power(x,n)  which means x to the power y.

def power(a,b):
    res=1
    for i in range(1, b+1):
        res=a*res
    return res

if __name__=="__main__":
    a=2
    b=5
    print(power(a,b))


# efficient method

def power_eff(a,b):
    if b == 0:
        return 1

    temp = power(a, b // 2)
    temp = temp * temp

    if b % 2 == 0:
        return temp
    else:
        return temp * a


if __name__=="__main__":
    a=2
    b=4
    print(power_eff(a,b))