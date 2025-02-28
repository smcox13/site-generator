import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()