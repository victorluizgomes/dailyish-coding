# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# something that reads the same backwards as forwards
  def isPalindrome(self, head: ListNode) -> bool:

      if head == None:
          return True

      curr = head
      lis = []
      while curr != None:
          lis.append(curr.val)

          curr = curr.next

      reverse = lis.copy()
      reverse.reverse()
      for i in range(0, len(lis)//2):
          if lis[i] != reverse[i]:
              return False

      return True
