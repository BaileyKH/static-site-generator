import unittest
from md_to_html import markdown_to_html_node

class TestMDToHtml(unittest.TestCase):

    def test_heading_to_h(self):
        md = "### This is a Heading Three"
        html = markdown_to_html_node(md)
        self.assertEqual(html.to_html(), '<div><h3>This is a Heading Three</h3></div>')

    def test_para_to_p(self):
        md = "This is a paragraph in markdown"
        html = markdown_to_html_node(md)
        self.assertEqual(html.to_html(), '<div><p>This is a paragraph in markdown</p></div>')

    def test_code_to_code(self):
        md = "```\nThis is a code block\n```"
        html = markdown_to_html_node(md)
        self.assertEqual(html.to_html(), '<div><pre><code>This is a code block</code></pre></div>')

    def test_quote_to_bquote(self):
        md = "> This is a quote"
        html = markdown_to_html_node(md)
        self.assertEqual(html.to_html(), '<div><blockquote>This is a quote</blockquote></div>')

    def test_unordered_to_ul(self):
        md = """
- Item one
- Item two
- Item three
"""
        html = markdown_to_html_node(md)
        self.assertEqual(html.to_html(), '<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>')

    def test_ordered_to_ol(self):
        md = """
1. Item one
2. Item two
3. Item three
"""
        html = markdown_to_html_node(md)
        self.assertEqual(html.to_html(), '<div><ol><li>Item one</li><li>Item two</li><li>Item three</li></ol></div>')