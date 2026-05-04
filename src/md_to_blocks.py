

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    strip_markdown = []

    for item in split_markdown:
        lines = item.split("\n")
        item = "\n".join([line.strip() for line in lines])
        item = item.strip()

        if item == "":
            continue

        strip_markdown.append(item)

    return strip_markdown