
N=int(input())
a=list(map(int,input().split()))
n=int(input())
s=""
for i in a:
    s+=str(i>>n)+" "
print(s)  


