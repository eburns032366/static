from textnode import TextNode, TextType
def main():

    print(TextNode("This is some anchor text", TextType.LINK, "http://www.somewhare.idk"))

if __name__ == "__main__":
    main()
