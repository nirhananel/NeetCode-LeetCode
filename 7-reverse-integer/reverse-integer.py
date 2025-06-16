class Solution:
    def reverse(self, x: int) -> int:
        y=0

        z = -1 if x<0 else 1

        x= abs(x)
        while x:
            a = x % 10
            y = y *10 + a
            x = x//10

        if y * z < -2**31 or y * z > 2**31 - 1:
         return 0
    
        return y*z