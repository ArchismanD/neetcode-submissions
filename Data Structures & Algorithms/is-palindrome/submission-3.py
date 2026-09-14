class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        rear = len(s) - 1

        while front < rear:
            while front < rear and not s[front].isalnum():
                front += 1
            while front < rear and not s[rear].isalnum():
                rear -= 1
            if s[front].lower() != s[rear].lower():
                return False
            else:
                front += 1
                rear -= 1
        return True

