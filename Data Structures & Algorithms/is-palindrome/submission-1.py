class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwardpointer = 0
        reversepointer = len(s) - 1

        while forwardpointer < reversepointer:
            while forwardpointer < reversepointer and not s[forwardpointer].isalnum():
                forwardpointer += 1
            while forwardpointer < reversepointer and not s[reversepointer].isalnum():
                reversepointer -= 1

            if s[forwardpointer].lower() != s[reversepointer].lower():
                return False

            forwardpointer += 1
            reversepointer -= 1

        return True