# test_linked_list.py

import unittest
from linked_list import Item, LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up a linked list with some initial items for testing."""
        self.linked_list = LinkedList()
        self.linked_list.insert(Item("Apple", 1.99))
        self.linked_list.insert(Item("Banana", 0.99))
        self.linked_list.insert(Item("Orange", 0.59))

    def test_insert(self):
        """Test inserting items into the linked list."""
        self.linked_list.insert(Item("Grapes", 2.50))
        items = self.linked_list.to_list()
        self.assertEqual(len(items), 4)
        self.assertEqual(items[-1].name, "Grapes")
        self.assertEqual(items[-1].price, 2.50)

    def test_delete_existing_item(self):
        """Test deleting an existing item from the linked list."""
        self.linked_list.delete("Banana")
        items = self.linked_list.to_list()
        self.assertEqual(len(items), 2)
        item_names = [item.name for item in items]
        self.assertNotIn("Banana", item_names)

    def test_delete_non_existing_item(self):
        """Test attempting to delete a non-existing item from the linked list."""
        self.linked_list.delete("Pineapple")
        items = self.linked_list.to_list()
        self.assertEqual(len(items), 3)  # List should remain unchanged

    def test_traverse(self):
        """Test traversing the linked list."""
        expected_items = [
            Item("Apple", 1.99),
            Item("Banana", 0.99),
            Item("Orange", 0.59)
        ]
        actual_items = self.linked_list.to_list()
        self.assertEqual(expected_items, actual_items)

if __name__ == '__main__':
    unittest.main()
