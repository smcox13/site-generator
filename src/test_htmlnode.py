import unittest

from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html1(self):
        node = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": "_blank",})
        print(node)

    def test_props_to_html2(self):
        node = HTMLNode("p", "this is a paragraph")
        print(node)

    def test_props_to_html3(self):
        node = HTMLNode("h1", "this is a header")
        print(node)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()