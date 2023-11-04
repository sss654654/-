# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 브루트 포스로 계산(타임아웃이에요)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                print(f'i:{i}, j:{j}')
                max_profit = max(prices[j]-prices[i], max_profit)

        return max_profit


# 저점과 현재 값과의 차이 계산
# 카데인 알고리즘? => 최대 서브 배열에서 사용
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # 최솟값(저점) 담을 변수
        min_price = sys.maxsize # 최댓값 담을 변수


        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)

        # print(max_profit)
        return max_profit



        