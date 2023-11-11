# https://leetcode.com/problems/reorder-data-in-log-files/


# https://github.com/CodingGuysGroup/Subin/blob/main/python%20libraries/lambda%2C%20key%20sort%20%EC%B4%9D%20%EC%A0%95%EB%A6%AC.md
# 람다와 + 연산자를 이용
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = []
        digit = []

        for log in logs:
            #print(log.split()[1], end = '')
            #print(log.split()[1].isdigit())
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letters.append(log)


        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digit
        

