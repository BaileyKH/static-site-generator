from textnode import TextType,TextNode

def split_nodes_delimiter(old_node, delimiter, text_type):
    new_nodes = []

    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split = node.text.split(delimiter)

        if len(split) % 2 == 0:
            raise Exception("No delimiter found")

        for index, item in enumerate(split):
            if not item:
                continue
            
            if index % 2 == 0:
                new_nodes.append(TextNode(item, TextType.TEXT))
            else:
                new_nodes.append(TextNode(item, text_type))

    return new_nodes