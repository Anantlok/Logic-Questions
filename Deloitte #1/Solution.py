n = int(input("enter the number of visiting students in their first line"))
a = list(map(int, input("number of space seperated ranks hod gets each time").split()))
m = a[0]
ans = 0
for i in range(1, n):
    if a[i] < m:
        m = a[i]
        ans += 1
print(ans)
