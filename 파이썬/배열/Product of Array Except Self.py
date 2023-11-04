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
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i] # p는 다음 i 이전 까지의 왼쪽의 모든 수를 곱한 값
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= p
            p *= nums[i] # p는 다음 i 이전 까지의 오른쪽의 모든 수를 곱한 값
        
        return out
            
            

