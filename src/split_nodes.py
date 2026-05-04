from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        extracted_images = extract_markdown_images(node.text)

        if len(extracted_images) == 0:
            new_node.append(node)
            continue

        remaining_text = node.text

        for alt, url in extracted_images:
            split_text = remaining_text.split(f"![{alt}]({url})")

            if split_text[0]:
                new_node.append(TextNode(split_text[0], TextType.TEXT))

            new_node.append(TextNode(alt, TextType.IMAGE, url))

            remaining_text = split_text[1]

        if len(remaining_text) != 0:
            new_node.append(TextNode(remaining_text, TextType.TEXT))

    return new_node

def split_nodes_link(old_nodes):
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        extracted_links = extract_markdown_links(node.text)

        if len(extracted_links) == 0:
            new_node.append(node)
            continue

        remaining_text = node.text

        for anchor, url in extracted_links:
            split_text = remaining_text.split(f"[{anchor}]({url})")

            if split_text[0]:
                new_node.append(TextNode(split_text[0], TextType.TEXT))

            new_node.append(TextNode(anchor, TextType.LINK, url))

            remaining_text = split_text[1]

        if len(remaining_text) != 0:
            new_node.append(TextNode(remaining_text, TextType.TEXT))

    
    return new_node