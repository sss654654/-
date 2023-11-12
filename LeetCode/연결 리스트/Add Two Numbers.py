# https://leetcode.com/problems/add-two-numbers/
# https://www.youtube.com/watch?v=H1ov8gTjuvk

# 자료형 변환

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while l1: # l1.next가 None이 되면 탈출
            list1.append(l1.val)
            l1 = l1.next

        while l2: # l1.next가 None이 되면 탈출
            list2.append(l2.val)
            l2 = l2.next

        # 문자열 리스트를 str로 변경 => 문자열 조작 Group Anagram
        # 숫자형 리스트를 str로 변경
        # 1. 숫자형 리스트 list1의 숫자 요소 e를 str로 감쌈
        # 2. join을 통해 각 문자를 합쳐서 숫자 str 
        # 3. join을 통해 생성된 str을 int로 형변환
       # print(int(''.join(str(e) for e in list1)))
       # print(int(''.join(str(e) for e in list2)))
        result_str =str(int(''.join(str(e) for e in list1)) + int(''.join(str(e) for e in list2)))


        node = None
        prev: ListNode = None
        for i in result_str:
            node = ListNode(i)
            node.next = prev
            prev = node
        
        return node
