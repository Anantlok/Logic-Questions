class Solution(object):
    def maximum69Number (self, num):
        nums = list(str(num))
        maxi = num
        for i in range(len(nums)):
            temp=nums[:]
            if temp[i] == "6":
                temp[i] = "9"
            elif temp[i] == "9":
                temp[i] = "6"
            new_num=int("".join(temp))
            maxi=max(maxi,new_num)
        return (maxi)


        