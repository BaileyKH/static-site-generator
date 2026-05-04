import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestMarkdownExtract(unittest.TestCase):

    def test_multi_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_multi_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_no_image(self):
        text = "This is just some plain text with no image attached"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [])

    def test_no_link(self):
        text = "This is just some plain text with no links attached"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [])

    def test_only_extract_links(self):
        text = "Here is a ![cat](https://cat.com/cat.png) and a [link](https://boot.dev)"
        extracted_link = extract_markdown_links(text)
        self.assertEqual(extracted_link, [("link", "https://boot.dev")])