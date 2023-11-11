# https://leetcode.com/problems/product-of-array-except-self/

# 내가 푼 풀이(시간초과)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            left, right = i-1, i+1
            left_mul = 1
            right_mul = 1
            while left >= 0:
                left_mul *= nums[left]
                left -= 1
            while right < len(nums):
                right_mul *= nums[right]
                right += 1# 
            
            new_nums.append(left_mul * right_mul)
        
       # print(new_nums)
        return new_nums

        
# 자신을 제외한 배열의 곱
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []
        p = 1 # 포인터의 첫번째는 왼쪽에 있는 값이 없으므로
        for i in range(len(nums)):
            out.append(p) # p는 포인터 좌측의 곱
            p *= nums[i]
        
        print(out)
        p = 1 # 포인터의 마지막은 오른쪽에 있는 값이 없으므로
        for i in range(len(nums)-1, -1, -1):
            out[i] *= p # p는 포인터 우측의 곱
            p *= nums[i]

        return out
            
            

