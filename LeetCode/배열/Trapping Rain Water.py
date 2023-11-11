# https://leetcode.com/problems/trapping-rain-water/
# https://www.youtube.com/watch?v=ZA5OpE2PeAg
# https://www.youtube.com/watch?v=Bgv-cV2Wcjs


# 투 포인터를 최대로 이동
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        left_max = height[left]
        right_max = height[right]
        volume = 0
        while left < right:

            # 이전 막대 최댓값 - 현재 막대 높이를 통해 물의 높이를 구하기 위해서 이전 막대기와 현재 막대기 중 큰 값을 저장
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            print(f'height[left]:{height[left]}, height[right]:{height[right]}')
            print(f'left_max:{left_max}, right_max:{right_max}')

            # 기본적으로 낮은 높이의 막대가 반대 방향으로 이동
            # 좌측 높이와 우측 높이가 같다면 좌측을 우측으로 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left+= 1
            else:
                volume += right_max - height[right]
                right -= 1
            print(f'volume:{volume}')
        return volume

# 스택 쌓기, FILO
class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []
        for i in range(len(height)):
            # 스택에 계속 쌓으면서
            # 변곡점(전보다 큰 높이의 막대기)을 만나면 스택에서 꺼냄, while 써서
            # 이전과의 차이만큼 물 높이 처리

            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i],height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)