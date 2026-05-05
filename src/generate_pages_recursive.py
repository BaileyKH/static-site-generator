import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entires = os.listdir(dir_path_content)

    for entry in entires:
        if entry.endswith(".md"):
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry.replace(".md", ".html")))

        if os.path.isdir(os.path.join(dir_path_content, entry)):
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))