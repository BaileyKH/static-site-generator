from md_to_blocks import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            return block[2:]
        
    raise Exception("No heading one found")
