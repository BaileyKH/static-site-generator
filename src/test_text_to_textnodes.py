import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToNodes(unittest.TestCase):

    def test_all_types(self):
        node = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        new_node = text_to_textnodes(node)
        self.assertListEqual(new_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_single_type(self):
        node = 'This is text with only **one** type within it'
        new_node = text_to_textnodes(node)
        self.assertListEqual(new_node, [
            TextNode("This is text with only ", TextType.TEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" type within it", TextType.TEXT)
        ])

    def test_no_type(self):
        node = "This is text with absolutely no types in it, just plain text"
        new_node = text_to_textnodes(node)
        self.assertEqual(new_node, [TextNode("This is text with absolutely no types in it, just plain text", TextType.TEXT)])
