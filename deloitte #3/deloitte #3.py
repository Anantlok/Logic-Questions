
def func(n, k):
    count = 0
    for num in range(n):  
        if bin(num).count('1') == k:  
            count += 1
    return count


n, k = map(int, input("upto which number you want to count and \
what amount of exact bits do you want the number to be elligible for").split())


print(func(n, k))

