# find if the number is palindrome or not, provided that, n>=0.

def palindrom_number(x: int) -> bool:
    revese_number = 0
    temp_number=x
    while (temp_number > 0):
        rd = temp_number % 10
        revese_number= revese_number * 10 + rd
        temp_number= temp_number // 10
    return x==revese_number

if __name__ == "__main__":
    number=3430343
    print(palindrom_number(number))
