import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.google.com", "target": "_blank"})

    def test_props_2(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.duckduckgo.com", "target": "_blank"})

    def test_no_props(self):
        node2 = HTMLNode("p", "Hello")

if __name__ == "__main__":
    unittest.main()
