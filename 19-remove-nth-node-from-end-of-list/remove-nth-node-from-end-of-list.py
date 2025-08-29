# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        length=0
        while current:
            length+=1
            current=current.next
        if n>length or n==0:
            return
        k=length-n
        current=head
        if n==length:
            head=head.next
            return head
        for i in range(k-1):
            current=current.next
        if current.next:
            current.next=current.next.next
        return head