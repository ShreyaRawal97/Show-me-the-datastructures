"""
Union and Intersection
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    elements = set()
    node = llist_1.head
    new_list = LinkedList()
    while node:
        if node.value not in elements:
            elements.add(node.value)
            new_list.append(node)

        node = node.next

    node = llist_2.head
    while node:
        if node.value not in elements:
            elements.add(node.value)
            new_list.append(node)

        node = node.next
    return new_list
    pass

def intersection(llist_1, llist_2):
    elements = set()
    node = llist_1.head
    new_list = LinkedList()
    while node:
        if node.value not in elements:
            elements.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value in elements:
            elements.remove(node.value)
            new_list.append(node)
        node = node.next

    return new_list
    pass


# Test case 1
print("Test Case 1 - ")
list1 = LinkedList()
list2 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
for i in element_1:
    list1.append(i)
for j in element_2:
    list2.append(j)

print (union(list1, list2)) #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print (intersection(list1, list2)) #6 -> 4 -> 21 ->

# Test case 2
print("Test Case 2 - ")
list3 = LinkedList()
list4 = LinkedList()
element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]
for i in element_3:
    list3.append(i)
for j in element_4:
    list4.append(j)
print (union(list3,list4)) #3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(list3,list4)) #

# Test case 3
print("Test Case 3 - ")
list5 = LinkedList()
list6 = LinkedList()
element_5 = []
element_6 = [9,6,7]
for i in element_5:
    list5.append(i)
for j in element_6:
    list6.append(j)
print (union(list5, list6)) #9 -> 6 -> 7 ->
print (intersection(list5, list6)) #
