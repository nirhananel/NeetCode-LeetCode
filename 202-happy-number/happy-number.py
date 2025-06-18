class Solution:
    def isHappy(self, n: int) -> bool:
        s,f = n, self.sumOfSquares(n)
        power = lam = 1

        while s != f:
            if power == lam:
                s = f
                power *= 2
                lam = 0
            f = self.sumOfSquares(f)
            lam += 1
        return True if f == 1 else False

    def sumOfSquares(self, n:int) -> int:
            output = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n= n// 10
            return output