# linked_list.py

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price})"

class Node:
    def __init__(self, item: Item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item: Item):
        """Inserts a new item into the linked list."""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, item_name: str):
        """Deletes the first occurrence of an item by name from the linked list."""
        current = self.head
        previous = None

        while current is not None and current.item.name != item_name:
            previous = current
            current = current.next

        if current is None:
            print(f"Item with name '{item_name}' not found.")
            return

        if previous is None:
            # Item to be deleted is the head
            self.head = current.next
        else:
            previous.next = current.next

        print(f"Item '{item_name}' deleted.")

    def traverse(self):
        """Traverses the linked list and prints each item."""
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def to_list(self):
        """Returns the linked list as a list of items."""
        items = []
        current = self.head
        while current is not None:
            items.append(current.item)
            current = current.next
        return items

# Sample usage
if __name__ == '__main__':
    # Create a new linked list
    linked_list = LinkedList()

    # Insert items into the linked list
    linked_list.insert(Item("Apple", 1.99))
    linked_list.insert(Item("Banana", 0.99))
    linked_list.insert(Item("Orange", 0.59))

    # Traverse and print all items in the linked list
    print("Items in the linked list:")
    linked_list.traverse()

    # Delete an item from the linked list
    linked_list.delete("Banana")

    # Traverse and print all items after deletion
    print("\nItems in the linked list after deletion:")
    linked_list.traverse()
