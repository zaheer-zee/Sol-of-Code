# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        num1 = ""
        num2 = ""
        head = l1
        curr = head
        while curr != None:
            num1 += str(curr.val)
            curr = curr.next 
        head = l2
        curr = head
        while curr != None:
            num2 += str(curr.val)
            curr = curr.next 
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = int(num1) + int(num2)
        
        result = str(result)
        anslis = []
        for i in range(len(result)-1,-1,-1):
            anslis.append(int(result[i]))
        head = ListNode(anslis[0])
        curr = head
        for i in range(1,len(anslis)):
            curr.next = ListNode(anslis[i])
            curr = curr.next
        return head



        


