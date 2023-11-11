# https://leetcode.com/problems/valid-palindrome/

# 리스트로 변환
class Solution:
    def isPalindrome(self, s: str) -> bool:

        strs= []
        for char in s:
            if char.isalnum(): # 숫자와 문자만을 체크
                strs.append(char.lower()) # 대문자 -> 소문자

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
        

# 데크 자료형을 이용한 최적화
from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:

        strs= deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
   
        
# 슬라이싱 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
        # 정규식 패턴
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1]