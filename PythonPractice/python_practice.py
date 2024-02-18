#This file consists of random code used to practice/retain Python skills
from collections import defaultdict

def containsDuplicates(nums):
  mySet = set()

  for n in nums:
    if n in mySet:
      return True
    mySet.add(n)
  return False

def validAnagram(str1, str2):
  if len(str1) != len(str2):
    return False
  
  dict1, dict2 = defaultdict(int), defaultdict(int)

  for i in range(len(str1)):
    dict1[str1[i]] += 1
    dict2[str2[i]] += 1

  for c in str1:
    if dict1[c] != dict2[c]:
      return False
  return True

def twoSum(nums, target):
  diff = 0
  myDict = defaultdict(int)

  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in myDict:
      return [i, myDict[diff]]
    myDict[nums[i]] = i
  return []

def productExceptSelf(nums):
    result = [1] * len(nums)          # list of len nums for output
    prefix = 1

                                      # input-> nums = [1,2,3,4]
    for i in range(len(nums)):        # prefix-> 1 [1,1,1,1] : this is what result is after each iteration
        result[i] = prefix            # prefix-> 2 [1,1,3,4]
        prefix *= nums[i]             # prefix-> 6 [1,1,2,4]
                                      # prefix-> 24[1,1,2,6]

    postfix = 1

    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

def string_match(a, b):
  length = 0
  count = 0
  if len(a) > len(b):
    length = len(b)
  else:
    length = len(a)
  
  for i in range(length-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

def group_anagrams(strs):
  result = defaultdict(list)

  for s in strs:
    count = [0]*26                    # for the 26 letters in the alphabet
    for c in s:
      index = ord(c) - ord('a')
      count[index] += 1
    result[tuple(count)].append(s)
  return result.values()

def removeElement(nums, val):
  index = 0

  while index < len(nums):
    if nums[index] != val:
      index += 1
    else:
      nums.pop(index)
  return index                        # for some reason, this problem on leetcode wants the index returned rather than the updated list with removed elements

def numUniqueEmails(emails):
  res = set()

  for email in emails:
    local = email.split('@')[0]       # this splits at the occurence of '@' and takes the front half '[0]' and stores into local
    domain = email.split('@')[1]
    temp = ""

    for c in local:
      if c != '+' and c != '.':
        temp += c
      if c == '+':
        break
    temp += "@"+domain
    if temp not in res:
      res.add(temp)
  return len(res)

def valid_palindrome(s):
  result = ""

  for c in s:
    if c.isalnum():
      result += c.lower()
  return result == result[::-1]

def maxProfit(prices):
  i, j = 0, 1
  maxProfit = 0

  while j < len(prices):
    if prices[i] < prices[j]:
      profit = prices[j] - prices[i]
      maxProfit = max(maxProfit, profit)
    else:
      i = j
    j += 1
  return maxProfit

def reverse_string_brute(s):
  index = len(s)-1
  reversed = ""

  while index >= 0:
    reversed += s[index]
    index -= 1
  return reversed

def reverse_string_simple(s):
  return s[::-1]

def reverseList(head):
  revList = None                          # we set what will be our reversed LinkedList to None
  current = head                          # we store the current head node to 'current'

  while current:                          # while we have a node saved to 'current'                                                 []->[]->[]->[]->None
    nextNode = current.next               # we store the node that 'current' is pointing at into 'nextNode'                  None <-[] x []->[]->[]
    current.next = revList                # we want our head node to point to None as it will be the end once reversed       None <-[]
    revList = current                     # here we're basically adding the now reveresed node into revList                         []->[]->[]
    current = nextNode                    # the next node to work with is now our nextNode
                                          #                                                                                  None <-[]<-[]<-[]<-[]
  return revList                          # by this point, the list should be reversed

def reverse_integer(num):
  reversed = 0

  while num != 0:
    reversed *= 10
    reversed += num % 10
    num //= 10
  return reversed

class ListNode():
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def mergeTwoLists(list1, list2):          # merging 2 LinkedLists
  head = current = ListNode()

  while list1 and list2:
    if list1.val < list2.val:
      current.next = list1.val
      list1 = list1.next
    else:
      current.next = list2.val
      list2 = list2.val
    current = current.next

    if list1:
      current.next = list1
    elif list2:
      current.next = list2

    return head.next
  
def validParenthesis(s):
  pList = []
  pDict = {")":"(","]":"[","}":"{"}

  for c in s:
    if c in "({[":
      pList.append(c)
    elif not pList or pList[-1] != pDict[c]:
      return False
    else:
      pList.pop()
  return len(pList) == 0

#call the main method
if __name__ == "__main__":
  #print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
  #print(containsDuplicates([1,3,5,7,3,20]))
  #print(validAnagram("anagram","nagaram"))
  #print(twoSum([3,2,4], 6))
  #print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
  print(valid_palindrome("A man, a plan, a canal: Panama"))
  #print(maxProfit([7,1,5,3,6,4]))
  #print(reverse_string_brute("apple"))
  #print(reverse_string_simple("teapot"))
  #print(reverse_integer(123))
  #print(validParenthesis("()[]{}"))