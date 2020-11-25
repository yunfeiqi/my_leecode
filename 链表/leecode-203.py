# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # defination
        sentinal = ListNode(0)
        sentinal.next = head

        # terminator
        if head is None:
            return head

        # process
        pre = sentinal
        cur = head
        while cur is not None:
            if cur.val == val:
                # delete current node
                pre.next = cur.next
            else:
                # previous node to right
                pre = cur

            # shift current ndoe
            cur = cur.next
        return sentinal.next


# 递归
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # terminator
        if head is None:
            return head

        # process
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
