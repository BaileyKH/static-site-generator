from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)

    return link