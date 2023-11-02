# https://leetcode.com/problems/3sum/

# 내가 푼거(5421ms)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # [-1,0,1,2,-1,-4]
        nums.sort()
        # [-4,-1,-1,0,1,2]
        ans = []

        for num in range(len(nums) - 2):
            
            left, right = num + 1, len(nums) - 1
            
            while left < right:
                zero = nums[num] + nums[left] + nums[right]

                if zero > 0:
                    right -= 1
                elif zero < 0:
                    left += 1
                else:
                    if [nums[num], nums[left], nums[right]] in ans:
                        left += 1
                        right -= 1
                        continue
                    ans.append([nums[num], nums[left], nums[right]])
                    left += 1
                    right -= 1
        
        print(ans)
        return ans


        

# 투 포인터로 합 계산
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort
        ans = []
# [-4,-1,-1,0,1,2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) -1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val < 0:
                    left += 1
                elif sum_val > 0:
                    right -= 1
                else:
                    ans.append([nums[i] ,nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans

'''
나는 [nums[i] ,nums[left], nums[right]]가 ans안에 있는지 확인하기 위해 
in을 써서 반복문 안에 O(n)을 추가해 엄청난 시간이 걸렸으나 다음 반복문은 
겹치는 문자가 있으면 건너뛰게 해주어 시간 복잡도를 대폭 줄임
'''
