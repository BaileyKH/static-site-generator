import os
from md_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

    with open(from_path, "r") as file:
        content = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    content_node = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    result = template.replace("{{ Title }}", title).replace("{{ Content }}", content_node).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(result)