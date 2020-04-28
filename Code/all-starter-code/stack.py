#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty

        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items

        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? O(1) because a single item is being added to the beginning of the list  """
        # TODO: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? O(1) because the item being removed is the head"""
        # TODO: Remove and return top item, if any

        if self.is_empty():
            raise ValueError("This stack is empty.")
        else:
            node = self.list.head.data
            self.list.delete(node)

            return node


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? O(1) because the item is added at the end of the list"""
        # TODO: Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        return self.list[self.length() - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? O(1) because it deletes the top item"""
        # TODO: Remove and return top item, if any

        if self.is_empty():
            raise ValueError("This stack is empty")
        remove = self.peek()
        self.list.remove(self.peek())
        return remove


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack


# """ Notes: TA Shaash

# In a stack, we have a l = [5, 2, 44] <-- (first in) 5, 2, 44 (last in)

# 44             last one in, needs to be the first one to remove 
# --
# 2              can only be removed once the last item (44) is removed
# --
# 5              first item in, will be the last one removed

# -  def push(item):
#     time complexity: O(1) because a single item is being added to the end of the list 
#     l.append(item)

#     ex) push(item):
    
#         l = [5, 2, 44]
#         l.append(30)

#         [5, 2, 44, 30]

#         30  (top)
#         --
#         44             
#         --
#         2              
#         --
#         5   (bottom)


# - def pop(item):
#     # time complexity: O(1) because it 
#     # deletes the top item

#     del l[len(1) - 1]

#     ex) pop()

#         [5, 2, 44, 30]

#         30  (top)
#         --
#         44             
#         --
#         2              
#         --
#         5   (bottom)



# - def peek():
#     # time complexity: 
#     return l[len(1) - 1]