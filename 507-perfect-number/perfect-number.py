class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        div=[1]
        i=2
        while i*i<=num:
            if num%i==0:
                div.append(i)
                if i!=num//i:
                    div.append(num//i)
            i=i+1
        return sum(div)==num
        