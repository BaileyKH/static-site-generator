from textnode import TextNode, TextType
from copy_static import copy_source_to_destination

def main():
    textnode = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')

    print(textnode)

    copy_source_to_destination("static", "public")

if __name__ == '__main__':
    main()