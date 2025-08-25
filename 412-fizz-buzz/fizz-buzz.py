class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ar=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ar.append("FizzBuzz")
            elif i%3==0:
                ar.append("Fizz")
            elif i%5==0:
                ar.append("Buzz")
            else:
                ar.append(str(i))
        return ar