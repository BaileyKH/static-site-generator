from textnode import TextNode, TextType
from copy_static import copy_source_to_destination
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    textnode = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

    print(textnode)

    copy_source_to_destination("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", base_path)

if __name__ == '__main__':
    main()