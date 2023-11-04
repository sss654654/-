# https://leetcode.com/problems/array-partition/
# https://www.youtube.com/watch?v=ZA5OpE2PeAg

# 오름차순 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        pair = []
        ans = 0
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                ans += min(pair)
                pair = []
        print(ans)

# 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans += nums[i]

        return ans