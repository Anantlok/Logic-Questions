
s1 = input()
s2 = input()
s3 = ""
def fun(i, j, k, s):
    global s1
    global s2
    global s3
    if i == len(s1) or j == len(s2):
        if len(s3) == len(s):
            s3 = min(s, s3)
        elif len(s3) < len(s):
            s3 = s
        return k
    if s1[i] == s2[j]:
        return fun(i + 1, j + 1, k + 1, s + s1[i])
    return max(fun(i + 1, j, k, s), fun(i, j + 1, k, s))
fun(0, 0, 0, "")
print(s3)

