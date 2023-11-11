# https://leetcode.com/problems/reverse-string/

# 투 포인터를 이용한 스왑
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = 0
        end = len(s) - 1

        while st < end:
            s[st], s[end] = s[end], s[st]
            st += 1
            end -= 1


# 파이썬다운 방식
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

