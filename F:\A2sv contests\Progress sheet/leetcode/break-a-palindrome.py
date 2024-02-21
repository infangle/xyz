class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ''

        for i in range(len(palindrome)):
            if palindrome == ['a']*len(palindrome):
                palindrome[-1] = 'b'
                break
            if palindrome[i] != 'a':
                prev = palindrome[i]
                palindrome[i] = 'a'
                if palindrome != palindrome[::-1]:
                    break
                else:
                    palindrome[i] = prev
            elif palindrome[i] == 'a' and i == len(palindrome) - 1:
                palindrome[-1] = 'b'

            
        return ''.join(palindrome)