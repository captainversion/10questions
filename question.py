## 1. Delete the elements in an linked list whose sum is equal to zero.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
 
#     def deleteNode(self, key):
         
#         temp = self.head
#         if (temp is not None):
#             if (temp.data == key):
#                 self.head = temp.next
#                 temp = None
#                 return
#         while(temp is not None):
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next
#         if(temp == None):
#             return
#         prev.next = temp.next
#         temp = None
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print (" %d" %(temp.data)),
#             temp = temp.next
 
# llist = LinkedList()
# llist.push(7)
# llist.push(1)
# llist.push(3)
# llist.push(2)
 
# print ("Created Linked List: ")
# llist.printList()
# llist.deleteNode(1)
# print ("Linked List after Deletion of 1:")
# llist.printList()

##------------------------------------------------------------------------------------------------------------------------------------

## 2.Reverse a linked list in groups of given size.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
  
#     def reverse(self, head, k):
        
#         if head == None:
#           return None
#         current = head
#         next = None
#         prev = None
#         count = 0
#         while(current is not None and count < k):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#             count += 1
#         if next is not None:
#             head.next = self.reverse(next, k)
#         return prev
  
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data,end=' ')
#             temp = temp.next
  
# llist = LinkedList()
# llist.push(9)
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)
  
# print("Given linked list")
# llist.printList()
# llist.head = llist.reverse(llist.head, 3)  
# print ("\nReversed Linked list")
# llist.printList()

##------------------------------------------------------------------------------------------------------------------------------------

##3.Merge a linked list into another linked list at alternate positions.

# class Node(object):
#     def __init__(self, data:int):
#         self.data = data
#         self.next = None
  
# class LinkedList(object):
#     def __init__(self):
#         self.head = None
          
#     def push(self, new_data:int):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
          
#     def printList(self):
#         temp = self.head
#         while temp != None:
#             print(temp.data)
#             temp = temp.next
              
#     def merge(self, p, q):
#         p_curr = p.head
#         q_curr = q.head
#         while p_curr != None and q_curr != None:
#             p_next = p_curr.next
#             q_next = q_curr.next
#             q_curr.next = p_next  
#             p_curr.next = q_curr  
#             p_curr = p_next
#             q_curr = q_next
#             q.head = q_curr

# llist1 = LinkedList()
# llist2 = LinkedList()
# llist1.push(3)
# llist1.push(2)
# llist1.push(1)
# llist1.push(0)

# for i in range(8, 3, -1):
#     llist2.push(i)
  
# print("First Linked List:")
# llist1.printList()
# print("Second Linked List:")
# llist2.printList()
# llist1.merge(p=llist1, q=llist2)
# print("Modified first linked list:")
# llist1.printList()  
# print("Modified second linked list:")
# llist2.printList()
  
##------------------------------------------------------------------------------------------------------------------------------------

## 4.In an array, Count Pairs with given sum.

# def getPairsCount(arr, n, sum):
 
#     count = 0  
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == sum:
#                 count += 1
#     return count
 
# arr = [1, 5, 7, -1, 5]
# n = len(arr)
# sum = 6
# print("Count of pairs is",
#       getPairsCount(arr, n, sum))
 
##-----------------------------------------------------------------------------------------------------------------------------------

##  5.Find duplicates in an array.

# def find_duplicates(arr):
#     duplicates = []
    
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j] and arr[i] not in duplicates:
#                 duplicates.append(arr[i])    
#     return duplicates

# nums = [1, 2, 3, 4, 4, 5, 6, 6, 7]
# print(find_duplicates(nums))

##-----------------------------------------------------------------------------------------------------------------------------------

## 6.Find the Kth largest and Kth smallest number in an array.

# def find(k, arr, l):
#     arr.sort(reverse=True)
#     print("K th maximum element is: ", arr[k - 1])
#     print("K th minimum element is: ", array[l - k])


# array = [1, 7, 6, 8, 9, 2, 4, 5, 3, 0]
# k = 2
# find(k, array, len(array))

##-----------------------------------------------------------------------------------------------------------------------------------

## 7.Move all the negative elements to one side of the array.

# def move_negatives(arr):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         while arr[left] < 0:
#             left += 1

#         while arr[right] >= 0:
#             right -= 1

#         if left <= right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     return arr

# arr = [4, -1, 5, -3, -2, -6, 8, -9]
# print("Original Array:", arr)

# arr = move_negatives(arr)
# print("Array after moving negatives to one side:", arr)

##----------------------------------------------------------------------------------------------------------------------------------

## 8.Reverse a string using a stack data structure.

# def reverse_string(string):
#     stack = []
#     reversed_string = ""
#     for char in string:
#         stack.append(char)
#     while len(stack) > 0:
#         reversed_string += stack.pop()
#     return reversed_string
# string = "Hello, world!"
# reversed_string = reverse_string(string)
# print("Original string:", string)
# print("Reversed string:", reversed_string)

##---------------------------------------------------------------------------------------------------------------------------------

## 9.Evaluate a postfix expression using stack.

# class Evaluate:
#     def __init__(self, capacity):
#         self.top = -1
#         self.capacity = capacity
#         self.array = []
#     def isEmpty(self):
#         return True if self.top == -1 else False
#     def peek(self):
#         return self.array[-1]
#     def pop(self):
#         if not self.isEmpty():
#             self.top -= 1
#             return self.array.pop()
#         else:
#             return "$"
#     def push(self, op):
#         self.top += 1
#         self.array.append(op)
#     def evaluatePostfix(self, exp):
#         for i in exp:
#             if i.isdigit():
#                 self.push(i)
#             else:
#                 val1 = self.pop()
#                 val2 = self.pop()
#                 self.push(str(eval(val2 + i + val1)))
#         return int(self.pop())
# if __name__ == '__main__':
#     exp = "231*+9-"
#     obj = Evaluate(len(exp))
     
#     print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))

# #------------------------------------------------------------------------------------------------------------------------------ 

# #10.Implement a queue using the stack data structure.

# class Queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
 
#     def enQueue(self, x):
#         while len(self.s1) != 0:
#             self.s2.append(self.s1[-1])
#             self.s1.pop()

#         self.s1.append(x)
#         while len(self.s2) != 0:
#             self.s1.append(self.s2[-1])
#             self.s2.pop()
 
#     def deQueue(self):
         
#         if len(self.s1) == 0:
#             return -1
#         x = self.s1[-1]
#         self.s1.pop()
#         return x
 
# if __name__ == '__main__':
#     q = Queue()
#     q.enQueue(1)
#     q.enQueue(2)
#     q.enQueue(3)
 
    # print(q.deQueue())
    # print(q.deQueue())
    # print(q.deQueue())
 


















