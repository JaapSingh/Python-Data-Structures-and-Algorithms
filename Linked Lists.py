# Linked Lists------------------------------------------------------------------
# Node
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def traversal(self):
        node = self
        while node != None:
            print(node.value)
            node = node.next

# Wrapper
class List:
    def __init__(self, head):
        self.head = head

# Example Linked List
node1 = Node(7)
node2 = Node(1)
node3 = Node(6)
node4 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4

node1a = Node(5)
node2a = Node(9)
node3a = Node(2)
node4a = Node(9)
node1a.next = node2a
node2a.next = node3a
node3a.next = node4a


list1 = List(node1)

# CTCI questions

# 2.1 remove duplicated
def removeDup(node):
    uniqueVals = []
    currNode = node.next
    prevNode = node
    uniqueVals.append(prevNode.value)

    while currNode != None:
        if currNode.value in uniqueVals:
            prevNode.next = currNode.next
        else:
            uniqueVals.append(currNode)
            prevNode = prevNode.next
        currNode = currNode.next
    return node

#node1.traversal()
#node1 = removeDup(node1)
#print("post dup removal")
#node1.traversal()

# 2.2 Return K'th to last
def kth(node, k):
    if k == 1:
        return node.value
    else:
        return kth(node.next, k-1)

def size(node, k):
    if node == None:
        return k
    else:
        return size(node.next, k+1)

def kth_from_end(node, k):
    length = size(node, 0)
    return kth(node, (length-k+1))

node1.traversal()
#node1 = removeDup(node1)
print("length is", size(node1, 0))
print("3th is ", kth(node1, 3))
print("2nd from end", (kth_from_end(node1, 2)))
#node1.traversal()

# partition according to a pivot
def partition(node, pivot):
    head = node
    tail = node

    while node != None:
        next = node.next
        if (node.value > pivot):
            tail.next = node
            tail = node
        else:
            node.next = head
            head = node
        node = next
        tail.next = None
    return head

#print("post partition")
#node1 = partition(node1, 50)
#node1.traversal()

# sum two integers in linked Lists
def sum_list(num1, num2):
    sum_ll = Node(0)
    head = sum_ll
    carryover = 0
    while ((num1 != None) or (num2 != None) or (carryover == 1)):
        sum_val = carryover
        if (num2 != None):
            sum_val += num2.value
            num2 = num2.next
        if (num1 != None):
            sum_val += num1.value
            num1 = num1.next
        carryover = 0
        if sum_val > 9:
            carryover += 1
            sum_val -= 10
        sum_ll.value = sum_val
        sum_ll.next = Node()
        sum_ll = sum_ll.next
    return head

# print("node1")
# node1.traversal()
# print("node1a")
# node1a.traversal()
# print("sum")
#(sum_list(node1, node1a)).traversal()

# find intersection of two linked Lists
def intersection(node1, node2):
    # find length of node1
    head1 = node1
    length1 = 0
    while (node1.next != None):
        length1 += 1
        node1 = node1.next

    # find length of node2
    head2 = node2
    length2 = 0
    while (node2.next != None):
        length2 += 1
        node2 = node2.next

    # basic intersection check
    if node1 != node2:
        return None

    if length1 >= length2:
        starting_point = length1 - length2
        while (starting_point != 0):
            head1 = head1.next
            starting_point -= 1
    else:
        starting_point = length2 - length1
        while (starting_point != 0):
            head2 = head2.next
            starting_point -= 1

    # compare both nodes for equivalency
    while (head1 != None):
        if head1 == head2:
            return head1
        else:
            head1= head1.next
            head2= head2.next
    return None

# print(intersection(node1, node1a))
