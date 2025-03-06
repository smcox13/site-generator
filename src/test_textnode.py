import unittest

from textnode import *
from htmlnode import *
from functions import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

class TestFunctions(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        print(f"Code Result: {split_nodes_delimiter([node], "`", TextType.CODE)}")
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ])
    
    def test_bold(self):
        node = TextNode("This is text with a **bold text** word", TextType.NORMAL)
        print(f"Bold Result: {split_nodes_delimiter([node], "**", TextType.BOLD)}")
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
        ])
    
    def test_italic(self):
        node = TextNode("This is text with a _italic text_ word", TextType.NORMAL)
        print(f"Italic Result: {split_nodes_delimiter([node], "_", TextType.ITALIC)}")
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ])

    def test_multiple(self):
        node = TextNode("This is text with a _italic text_ and **bold text** word", TextType.NORMAL)
        step1 = split_nodes_delimiter([node], "_", TextType.ITALIC)
        step2 = split_nodes_delimiter(step1, "**", TextType.BOLD)
        print(f"Italic Result 1/2: {step1}")
        print(f"Bold Result 2/2: {step2}")
        self.assertEqual(split_nodes_delimiter(step2, "**", TextType.BOLD), [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" and ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(" word", TextType.NORMAL),
        ])

if __name__ == "__main__":
    unittest.main()