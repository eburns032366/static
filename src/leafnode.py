class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        ostring = ""
        if self.props == None:
            return ""
        for k in self.props:
            ostring = ostring + f" {k}=\"{self.props[k]}\""
        return ostring

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
