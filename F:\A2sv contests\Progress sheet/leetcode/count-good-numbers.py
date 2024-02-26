class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def fast_pow(base: int, exp: int) -> int:
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result

        even_choices = fast_pow(5, (n + 1) // 2)
        odd_choices = fast_pow(4, n // 2)

        total_choices = (even_choices * odd_choices) % mod

        return total_choices

