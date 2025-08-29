# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rsum(self, node: ListNode):
        current=node
        sums=""
        while current:
            sums=sums+str(current.val)
            current=current.next
        return int("".join(reversed(sums)))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=self.rsum(l1)
        b=self.rsum(l2)
        result=a+b
        dummy=ListNode(0)
        current=dummy
        for d in str(result)[::-1]:
            current.next=ListNode(int(d))
            current=current.next
        return dummy.next