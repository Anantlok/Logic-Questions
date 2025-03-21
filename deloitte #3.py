"""
Question 3 : Help of Prepsters
Problem Statement :

Arnab has given me a challenge. I have to calculate the number of numbers 
which are less than a certain value n, and have exactly k set bits in its 
binary form. As you are a Prepster like me, help me write a code that will 
take input for n and k and give the expected output.

Constraints :
1<=n<=10000
1<=k<=10
Input Format :
First line containing n and k space separated
Output Format :
Number of numbers present in a single line

Sample Input:
7 2
Sample Output:
3
Explanation:
11,110,101 -> These three numbers.
""" 
def func(n, k):
    count = 0
    for num in range(n):  
        if bin(num).count('1') == k:  
            count += 1
    return count


n, k = map(int, input("upto which number you want to count and \
what amount of exact bits do you want the number to be elligible for").split())


print(func(n, k))
