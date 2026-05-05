from textnode import TextNode, TextType
from copy_static import copy_source_to_destination
from generate_pages_recursive import generate_pages_recursive

def main():
    textnode = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

    print(textnode)

    copy_source_to_destination("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == '__main__':
    main()