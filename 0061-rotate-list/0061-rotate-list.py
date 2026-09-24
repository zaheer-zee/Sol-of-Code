# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head 
        while curr != None:
            count += 1
            curr = curr.next
        if head == None:
            return None
        if head.next == None:
            return head
        if k == count or k == 0:
            return head
        elif k < count:
            curr = head
            f = head
            for i in range(count - k - 1):
                curr = curr.next
            head = curr.next 
            curr.next = None
            curr = head 
            while curr.next != None:
                curr = curr.next
            curr.next = f
            return head
        elif k > count:
            sp = k % count
            if sp == 0:
                return head
            curr = head
            f = head
            for i in range(count - sp - 1):
                curr = curr.next
            head = curr.next 
            curr.next = None
            curr = head 
            while curr.next != None:
                curr = curr.next
            curr.next = f
            return head


            
        