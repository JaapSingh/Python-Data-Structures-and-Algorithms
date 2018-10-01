#differnet types of trees:
# BST has ordering property
# in order: left, cur, right
# pre order: cur, left, right
# post order: left, right, cur
# MinHeap is essentially a BST, without ordering propery (i.e. complete)
  # can perform insert with bubble up in O(logn), and remove min in O(logn)
# tries are used for strings, and one of your children will be a null node if it makes a word
  # allows you to check if string is prefix of word in O(k) time (same as hash)

# a graph is just a series of nodes with edges connecting them
  # you need a wrapper in case you have unconnected nodes
# Depth vs breadth search
  # BFS is usually better for finding a path
  # NOT RECURSIVE. keep a queue of neighbours, and then iterate over them
  # Add neighbours all to queue, then dequeue and work on each node, iteratively

class Node:
    def __init__(self, value= None):
        self.value = value
        self.right = None
        self.left = None
    def __str__(self):
        return str(self.value)

# test input
my_array = [1, 2, 3, 4, 5, 6]
my_node= Node(3)
my_node.left = Node(2)
my_node.right = Node(4)

t= Node(4)
t.left = Node(2)
t.right = Node(5)
t.left.left = Node(1)
t.left.right = Node(3)

array_tree = Node()
# for element in my_array:
    # insert(array_tree, element)

# inserts value as a node into root
def insert(root, value):
    # if empty node, add value to root and return
    if root.value is None:
        root.value = value
        return
    # if value is less than root, recurse on left
    if (value <= root.value):
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    # if value is greater than root, recurse on right
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)
#inserts a sorted array into a balanced BST
def insert_array(node, array):
    if array:
        mid = (len(array))/2
        insert(node, array[mid])
        insert_array(node, array[:mid])
        insert_array(node, array[mid+1:])

# DFS Print
def print_tree_DFS(node):
    if node is None: return
    print_tree(node.left)
    print(node.value)
    print_tree(node.right)

# BFS Print
def print_tree_BFS(node):
    level = [node]
    while level:
        print(" ".join(str(element)for element in level))
        next_list=list()
        for element in level:
            if element.left:
                next_list.append(element.left)
            if element.right:
                next_list.append(element.right)
        level = next_list

print_tree_BFS(my_node)
insert_array(array_tree, my_array)
#print_tree_BFS(array_tree)

def height(node):
    if (node == None):
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1

def check_balanced(node):
    if abs(height(node.left) - height(node.right)) > 1:
        return False
    else:
        return True
unbalanced_tree = Node(1)
insert(unbalanced_tree, 2)
insert(unbalanced_tree, 3)
insert(unbalanced_tree, 4)
print_tree_BFS(unbalanced_tree)
print(height(unbalanced_tree))
print(check_balanced(unbalanced_tree))
