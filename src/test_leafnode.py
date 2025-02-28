import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print(f"Result P: {node}")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        print(f"Result Link: {node}")
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')
    
    def test_leaf_to_html_header(self):
        node = LeafNode("h1", "Hello, world!")
        print(f"Result Header: {node}")
        self.assertEqual(node.to_html(), '<h1>Hello, world!</h1>')
    


if __name__ == "__main__":
    unittest.main()