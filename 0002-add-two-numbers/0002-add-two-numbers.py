# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def trav(head):
            k=""
            current=head
            while current:
                k=k+str(current.val)
                current=current.next
                print(k)
            return "".join(reversed(k))
        k=int(trav(l1))+int(trav(l2))
        x="".join(reversed(str(k)))
        head=ListNode(int(x[0]))
        curr=head
        for val in x[1:]:
            curr.next=ListNode(int(val))
            curr=curr.next
        return head