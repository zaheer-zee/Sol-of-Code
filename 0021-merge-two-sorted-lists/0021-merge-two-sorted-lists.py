# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = []
        right = []
        head1 = list1
        head2 = list2
        curr1 = head1
        curr2 = head2
        while curr1 is not None:
            left.append(curr1.val)
            curr1 = curr1.next
        while curr2 is not None:
            right.append(curr2.val)
            curr2 = curr2.next
            
        def merge(left,right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                elif left[i] >= right[j]:
                    result.append(right[j])
                    j += 1
                # elif left[i] == right[j]:
                #     result.append(left[i])
                #     result.append(right[j])
                #     i += 1
                #     j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result
        result = merge(left,right)

        if len(result) != 0:
            head = ListNode(result[0])
        else:
            return None
        curr = head
        for i in range(1,len(result)):
            curr.next = ListNode(result[i])
            curr = curr.next
        return head



