import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_multiprop(self):
        node = HTMLNode("p", "This is a value", None, {"href": "https://www.google.com", "target": "blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="blank"')

    def test_noprops(self):
        node = HTMLNode("p", "This is a value", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_oneprop(self):
        node = HTMLNode("p", "This is a value", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click Me!</a>')

    def test_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")

    def test_no_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)


class TestParentNode(unittest.TestCase):
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

    def test_no_children(self):
        parent_node = ParentNode("p", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_multi_child(self):
        child_one = LeafNode("b", "Bold Text")
        child_two = LeafNode("p", "This is paragraph text")
        child_three = LeafNode(None, "None")
        parent_node = ParentNode("div", [child_one, child_two, child_three])

        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Bold Text</b><p>This is paragraph text</p>None</div>"
        )

    def test_parent_no_tag(self):
        child_node = LeafNode("p", "Paragraph Text")
        parent_node = ParentNode(None, [child_node])

        self.assertRaises(ValueError, parent_node.to_html)
    
if __name__ == "__main__":
    unittest.main()