# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=''
        num2=''
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        n1=num1[::-1]
        n2=num2[::-1]
        result = int(n1)+int(n2)        
        s=str(result)
        t=s[::-1]
        temp=None
        head=temp
        for i in range(len(t)):            
            l=ListNode(int(t[i]))
            if temp==None:
                temp=l
                head=temp
            else:
                temp.next=l
                temp=temp.next
        return head

