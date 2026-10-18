# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        lis = []
        curr = head
        while curr != None:
            lis.append(curr.val)
            curr = curr.next
        if len(lis) == 0:
            return None

        lis.sort()
        
        head = ListNode(lis[0])
        curr = head
        for i in range(1,len(lis)):
            curr.next = ListNode(lis[i])
            curr = curr.next

        return head



        
        