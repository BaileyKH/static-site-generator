import unittest
from md_to_blocks import markdown_to_blocks

class TestBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_newlines(self):
        md = """
    This is a bunch of text



    with a lot of new lines






    like a ton
    """
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a bunch of text",
                "with a lot of new lines",
                "like a ton"
            ]
        )

    def test_one_block(self):
        md = """
        This is a singular block
    """
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a singular block"])