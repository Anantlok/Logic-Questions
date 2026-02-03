# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        dumy=ListNode(0)
        dumy.next=head
        prev=dumy
        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        prev_sub=None
        for i in range(right-left+1):
            nextt=curr.next
            curr.next=prev_sub
            prev_sub=curr
            curr=nextt
        prev.next.next=curr
        prev.next=prev_sub
        return dumy.next