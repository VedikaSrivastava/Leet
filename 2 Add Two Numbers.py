# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getNumbers(self, l):
        num = []
        while True:
            num.append(l.val)
            l = l.next
            if l is None:
                break
        num.reverse()
        num = int("".join(map(str, num)))

        return num

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = self.getNumbers(l1) + self.getNumbers(l2)
        digits = list(map(int, str(num)))[::-1]
        head = ListNode(0)
        curr = head
        for n in digits:
            curr.next = ListNode(n)
            curr = curr.next
        return head.next
