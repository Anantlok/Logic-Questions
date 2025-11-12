class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        import sys
        def convert(x):
            if len(x)>4300:
                sys.set_int_max_str_digits(10000)
            return int(x)
        st1=convert(num1)
        st2=convert(num2)
        summ=str(st1+st2)
        return summ
        