# https://leetcode.com/problems/longest-palindromic-substring/
# https://www.youtube.com/watch?v=Xn676-fLq7I


# 중앙을 중심으로 확장하는 풀이

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            # 팰린드롬 판별 조건문
           
            while left >= 0 and right < len(s) and s[left] == s[right]: 
            # left나 right가 범위를 벗어나면 while 빠져나옴
            # left와 right가 같지 않으면 while 빠져나옴

            # 즉, 해당 반복문 들어온 순간부터 s는 팰린드롬 확정

            # 팰린드롬이 확정된 상태에서 양옆으로 더 뻗어봄
                left -= 1
                right += 1

            # 만약 양옆으로 뻗어봐서 팰린드롬이 아니다? 그럼 빠져나가
            
            print()
            return s[left + 1:right] 
            # left에 +1을 하는 이유는 반복문에서 빠져나올 때 팰린드롬에서 양옆으로 한단어씩 더해서 팰린드롬이 안되었기 때문임
            # 같은 이유로 right까지 슬라이싱은 right를 포함하지 않음

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 팰린드롬은 aba, bb등 홀수나 짝수의 형태로 존재한다.
        # 1개의 문자는 팰린드롬이 아니다.("a")
        # 고로 길이가 3과 2인 슬라이딩 윈도우를 움직인다.
        # 움직이다가 팰린드롬 판별되면 거기서 좌, 우로 뻗어나가며 팰린드롬 판별
        # 이는 expand 함수로 구현해놓음

        for i in range(len(s)-1):
# 반복문을 쓰는 이유는 팰린드롬 판별을 위해 홀수, 짝수의 슬라이딩 윈도우를 한칸씩 옮기기 위함임

            result = max(result,
                        expand(i,i+1),
                        expand(i,i+2),
                        key=len)
            # expand

            #print(expand(i,i+1))
        return result