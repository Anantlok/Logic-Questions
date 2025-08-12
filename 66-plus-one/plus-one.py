class Solution(object):
    def plusOne(self, digits):
        con=""
        for i in range(0,len(digits)):
            con=con+str(digits[i])
        don=int(con)+1
        don=list(str(don))
        ret=[]
        for i in range(0,len(don)):
            ret.append(int(don[i]))
        return ret

        