

# import pickle

# from oops.person import Person

# p = Person('shiv', 27, 'shiv@gmail.com')

# with open('persons.txt', 'wb') as file:
#     pickle.dump(p, file)
#     print('pickling the person obj is Done!')

# with open('persons.txt', mode='rb') as f:
#     p1 = pickle.load(f)
#     print(p1.name, p1.age, p1.mail)
#     print('object got unpickled')

# def is_even(num: int) -> bool:
#     return True if num % 2 == 0 else False

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

# print(tuple(map(str, nums)))
# print(tuple(filter(lambda num: True if num % 2 == 0 else False, nums)))

# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     lst1 = []
#     def get_vals(self, list1):
#         while True:
#             Solution.lst1.append(list1.val)
#             if isinstance(list1.next, ListNode):
#                 self.get_vals(list1.next)
#             else:
#                 break

#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         self.get_vals(list1)
#         self.get_vals(list2)

#         print(Solution.lst1)

# #  
# list1 = ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
# list2 = ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}

# s = Solution()
# s.get_vals

# import math

# def isPerfectSquare(num: int) -> bool:
#     return True if math.sqrt(num) % 1 == 0 else False

# print(isPerfectSquare(16))

from mysql.connector import connect as mysql

conn = mysql(host='localhost', user='root', password='Aug2023', port=3306, database = 'oracle')

print('connected to DB!')

cursor = conn.cursor()

cursor.execute('Drop table employee  ')
conn.commit()

result = cursor.fetchall()
print(result)
print('query executed perfectly!!!')