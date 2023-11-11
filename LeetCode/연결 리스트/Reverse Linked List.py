# https://leetcode.com/problems/reverse-linked-list/

# 재귀 구조로 뒤집기
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node: ListNode, prev:ListNode = None):
            if not node:
                return prev
            nex, node.next = node.next, prev
            # nex= node.next로 2,3,4,5가 담김

            # node는 1,2,3,4,5 에서 부터
            # 처음 node.next = None을 받고 node = 1이됨
            # node = 1은 reverse의 prev로 전달되며
            # reverse(2>3>4>5, 1>None)

            # 이제 node = 2>3>4>5가 되고 
            # prev = 1>None이 되며
            # nex = node.next(3>4>5)
            # node.next = prev(1>None)로 인해
            # node = 2>1>None이되며
            # 재귀를 통한 뒤집기가 성공
            
            return reverse(nex,node)
        
        return reverse(head)
        

# 반복 구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node: # node가 None이 되면 탈출
            next, node.next = node.next, prev
            node, prev = next, node

        return prev
