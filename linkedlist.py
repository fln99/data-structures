"""
The implementation below is a study case.
"""

class Element():
  
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
  
    def __init__(self, head=None):
        self.head = head
        

    def append(self, element):
        """Add the element at the end"""
        if not isinstance(element, Element):
            raise TypeError("The given argument's type is not valid.")
        
        if not self.head:
            self.head = element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = element


    def remove(self, value):
        """In case the value is not in the linked list, just does nothing"""
        if not isinstance(value, int):
            raise ValueError("Only integer data type is allowed as value.")

        previous = None
        current = self.head
        index = 0

        while current:
            if current.value == value:
                if index:
                    previous.next = current.next
                else:
                    self.head = current.next
            previous = current
            current = current.next
            index += 1

            
    def insert(self, element, index):
        """Index start at 0"""
        if not isinstance(element, Element):
            raise TypeError("The given argument's type is not valid.")
        
        if index > self.get_length() - 1:
            raise IndexError("The index is greater than the list size.")

        previous = None
        current = self.head
        count = 0

        while current:
            if count == index:
                if previous:
                    previous.next = element
                    element.next = current
                else:
                    element.next = current
                    self.head = element
            previous = current
            current = current.next
            count += 1


    def get_length(self):
        """Simply returns the length"""
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count


    def __str__(self):
        """Show linked list nodes and links"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return ' -> '.join(elements)
      
      
