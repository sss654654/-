# https://leetcode.com/problems/merge-two-sorted-lists/

# 재귀 구조로 연결
# 재귀 바킹독 : https://www.youtube.com/watch?v=8vDDJm5EewM
# 백트래킹 바킹독 : https://www.youtube.com/watch?v=Enz2csssTCs
# 재귀 백준 : https://www.acmicpc.net/workbook/view/7314
# 백트래킹 백준 : https://www.acmicpc.net/workbook/view/7315

# 재귀 구조로 연결
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or (list2 and list2.val < list1.val):
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


        