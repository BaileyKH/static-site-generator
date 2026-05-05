from md_to_blocks import markdown_to_blocks
from block_type import block_to_block_type, BlockType
from htmlnode import ParentNode, HTMLNode, LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        type = block_to_block_type(block)

        if type == BlockType.HEADING:
            children.append(heading_to_html_node(block))
        elif type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html_node(block))
        elif type == BlockType.CODE:
            children.append(code_to_html_node(block))
        elif type == BlockType.QUOTE:
            children.append(quote_to_html_node(block))
        elif type == BlockType.UNORDERED:
            children.append(unordered_to_html_node(block))
        elif type == BlockType.ORDERED:
            children.append(ordered_to_html(block))

    return ParentNode('div', children)

# |--------------------------------------------------|
# |   Helper Functions for Block Type to HTML Node   |
# |--------------------------------------------------|

def text_to_children(text):
    text_node = text_to_textnodes(text)
    html_nodes = []

    for node in text_node:
        new_node = text_node_to_html_node(node)
        html_nodes.append(new_node)

    return html_nodes


def heading_to_html_node(block):
    level = 0

    for char in block:
        if char == "#":
            level += 1
        else:
            break

    heading_text = block[level + 1:]
    children = text_to_children(heading_text)

    return ParentNode(f'h{level}', children)

def paragraph_to_html_node(block):
    new_para = block.replace('\n', " ")

    children = text_to_children(new_para)

    return ParentNode('p', children)

def code_to_html_node(block):
    new_code = block.replace('`', "").strip()
    text_node = TextNode(new_code, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)

    code_node = ParentNode('code', [html_node])
    return ParentNode('pre', [code_node])

def quote_to_html_node(block):
    split_block = block.split("\n")
    stripped_lines = [line.lstrip(">").strip() for line in split_block]
    new_text = "\n".join(stripped_lines)

    children = text_to_children(new_text)

    return ParentNode('blockquote', children)

def unordered_to_html_node(block):
    split_block = block.split("\n")
    stripped_lines = [line.lstrip("- ").strip() for line in split_block]
    list_items = []

    for line in stripped_lines:
        children = text_to_children(line)
        list_items.append(ParentNode('li', children))

    return ParentNode('ul', list_items)

def ordered_to_html(block):
    split_block = block.split("\n")
    list_items = []

    for line in split_block:
        split_line = line.split(". ", 1)[1]
        children = text_to_children(split_line)
        list_items.append(ParentNode('li', children))

    return ParentNode('ol', list_items)