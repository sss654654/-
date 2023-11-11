# https://leetcode.com/problems/palindrome-linked-list/
# https://www.youtube.com/watch?v=QEXQEM7z7pM


# 내 풀이(605ms)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        linked_list = []

        while True:
            if node.next == None: # 끝 노드
                linked_list.append(node.val)
                break
            linked_list.append(node.val)
            node = node.next

        if linked_list == linked_list[::-1]:
            return True
        
        return False

# 리스트 변환(1000ms)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        linked_list = []

        while node is not None:
            linked_list.append(node.val)
            node = node.next

        while len(linked_list) > 1:
            if linked_list.pop(0) != linked_list.pop():
                return False
        
        return True

# 데크를 이용한 최적화(560~580ms)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        deque = collections.deque()

        while node is not None:
            deque.append(node.val)
            node = node.next

        while len(deque) > 1:
            if deque.pop() != deque.popleft():
                return False
        
        return True


# 런너를 이용한 우아한 풀이
# https://ihp001.tistory.com/70?category=815852
'''
런너 기법이란?
연결 리스트 순회 시 2개의 포인터를 동시에 사용하는 기법
한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 
중간 위치, 길이 등을 판별할 때 유용하게 사용
'''
# 파이썬 다중할당 -> https://ihp001.tistory.com/71
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None # slow 런너(연결 리스트)의 역순
        slow = head
        fast = head

        while fast and fast.next:
            print(f"rev:{rev}\nfast:{fast}\nslow:{slow}\n")
            print()
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            #
            '''
rev를 1, slow를 2->3으로 가정, 즉 slow.next는 3

한줄의 경우
rev, rev.next, slow = slow, rev, slow.next

1 Transaction
rev = 2->3, rev.next = 1, slow = 3 -> rev = 2->1, slow = 3

만약 두 줄로 늘어트릴 경우
rev, rev.next = slow, rev
slow = slow.next

1 Transaction
rev = 2->3, rev.next = 1 -> rev = 2->1

* 여기서 중요한 점은 rev = slow로 인해 둘은 동일한 참조이므로 rev = 2->1이면 slow = 2->1이다.

따라서 다음 트랜잭션에서는
2 Transaction
slow = 1(slow = slow.next)


rev, rev.next = slow, rev라는 구문에서 slow와 rev가 동일한 참조가 됨

            '''
            
        print(f"rev:{rev}\nfast:{fast}\nslow:{slow}\n")

        if fast: 
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

