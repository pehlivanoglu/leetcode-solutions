class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_num = 0
        orig_num = x

        while x > 0:
            digit = x % 10
            rev_num = rev_num * 10 +digit
            x //= 10
        
        if rev_num == orig_num:
            return True
        
        return False
