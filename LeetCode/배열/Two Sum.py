# https://leetcode.com/problems/two-sum/
# https://www.youtube.com/watch?v=PWADVtWyE9Q

# 브루트포스로 계산(2595ms)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

        

# in을 이용한 탐색(378ms)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target - num in nums[i+1:]:
                return [i,nums[i+1:].index(target - num) + i + 1]


# 첫 번째 수를 뺀 결과 키 조회(70ms)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [i,dic[target-num]]
            dic[num] = i


# 투 포인터
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st,end = 0, len(nums) - 1

        while True:
            if nums[st]+ nums[end] == target:
                return [st,end]
            end -= 1
            if st == end:
                st += 1
                end = len(nums) -1