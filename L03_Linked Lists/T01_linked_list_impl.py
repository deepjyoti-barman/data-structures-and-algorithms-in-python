'''
    @description Implementation of Linked List in Python
    @author Deepjyoti Barman
    @date 31-Aug-2024
'''
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.link = None

class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: int) -> bool:
        new_node = Node(value)

        # When linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # When linked list has at least one node in it
        self.tail.link = new_node
        self.tail = new_node
        self.length += 1

        return True

    def prepend(self, value: int) -> bool:
        new_node = Node(value)

        # When linked list is empty
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        # When linked list has at least one node in it
        new_node.link = self.head
        self.head = new_node
        self.length += 1

        return True

    def pop(self) -> Node:
        # When linked list is empty
        if self.length == 0:
            return None

        # When linked list has only one node
        if self.length == 1:
            temp = self.head
            self.length -= 1
            self.head = None
            self.tail = None
            return temp.value

        # When linked list has more than one node
        pre = self.head
        temp = self.head

        # while temp.next is not None:
        # Traverse until temp (which is having instance of head) and tail are pointing to same node
        while temp is not self.tail:
            pre = temp
            temp = temp.link

        pre.link = None
        self.tail = pre
        self.length -= 1

        return temp

    def pop_optimized(self) -> Node:
        # When linked list is empty
        if self.length == 0:
            return None

        # When linked list has more than one node
        pre = self.head
        temp = self.head

        while temp.link is not None:
            pre = temp
            temp = temp.link

        self.tail = pre
        self.tail.link = None
        self.length -= 1

        # When linked list has only one node
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def pop_first(self) -> Node:
        # When linked list is empty
        if self.length == 0:
            return None

        # When linked list has only one node
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        # When linked list has more than one node
        temp = self.head
        self.head = self.head.link
        temp.link = None
        self.length -= 1
        return temp

    def pop_first_optimized(self) -> Node:
        # When linked list is empty
        if self.length == 0:
            return None

        # When linked list has more than one node
        temp = self.head
        self.head = self.head.link
        temp.link = None
        self.length -= 1

        # When linked list has more than one node
        if self.length == 0:
            self.tail = None

        return temp

    def get_value(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.link

        return temp

    def set_value(self, index: int, value: int) -> bool:
        temp = self.get_value(index)

        if temp is not None:
            temp.value = value
            return True

        return False

    def print_length(self):
        return self.length

    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.link
        print()


# Usage
linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.prepend(4)
linked_list.print_linked_list()
print(f'Length: {linked_list.print_length()}')
print()

print(f'Popped item: {linked_list.pop().value}')
linked_list.print_linked_list()
print(f'Length: {linked_list.print_length()}')
print()

print(f'Popped item: {linked_list.pop_first_optimized().value}')
linked_list.print_linked_list()
print(f'Length: {linked_list.print_length()}')
print()

item_index = int(input('Enter the index to fetch the item: '))
print(f'Item: {linked_list.get_value(item_index).value}')
item_value = int(input('Enter the value to replace the item: '))
linked_list.set_value(item_index, item_value)
linked_list.print_linked_list()
