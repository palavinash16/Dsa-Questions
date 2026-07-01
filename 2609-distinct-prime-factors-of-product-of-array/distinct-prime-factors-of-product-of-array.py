class Solution(object):
    def distinctPrimeFactors(self, nums):
        primeFactors = set()

        for num in nums:

            d = 2

            while d * d <= num:

                while num % d == 0:
                    primeFactors.add(d)
                    num //= d

                d += 1

            if num > 1:
                primeFactors.add(num)

        return len(primeFactors)
        