# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        sum = l1.val + l2.val
        if sum > 9:
            sum = 0
            c = 1
        l3 = ListNode(sum)
        sum = l1.next.val + l2.next.val
        if sum > 9:
            sum = 0
            l3.next = ListNode(sum + c)
            c = 1
        else:
            l3.next = ListNode(sum + c)
        sum = l1.next.next.val + l2.next.next.val
        if sum > 9:
            sum = 0
            l3.next.next = ListNode(sum + c)
        else:
            l3.next.next = ListNode(sum + c)

        return l3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
