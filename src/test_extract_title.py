import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_heading_one(self):
        md = "# This is a Heading!"
        title = extract_title(md)

        self.assertEqual(title, "This is a Heading!")

    def test_heading_three(self):
        md = "### This is a Heading Three!"

        with self.assertRaises(Exception):
            extract_title(md)

    def test_multi_line(self):
        md = """
This is a paragraph

This is another paragraph,

# And here is my heading!
"""

        title = extract_title(md)

        self.assertEqual(title, "And here is my heading!")