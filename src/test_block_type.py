import unittest
from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):

    def test_code_block(self):
        md = "```\nThis is a block of code\n```"
        block_type = block_to_block_type(md)

        self.assertEqual(block_type, BlockType.CODE)

    def test_no_type(self):
        md = 'This is just a paragraph of text'
        block_type = block_to_block_type(md)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        md = md = "1. This is item one\n2. This is item two\n3. This is item three"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED)

    def test_unordered_list(self):
        md = "- This is item one\n- This is item two\n- This is item three"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED)

    def test_heading(self):
        md = "### This is a Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_quote(self):
        md = "> This is a quote"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)