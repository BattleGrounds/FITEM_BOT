import xml.etree.ElementTree as ET

class Database:
    def __init__(self) -> None:
        self.file = ET.parse("db.xml")
        self.root = self.file.getroot()
    def __del__(self):
        with open("db.xml", "wb") as f:
            f.write(ET.tostring(self.file))
    def add_article(self, name, text):
        article = ET.SubElement(self.root, "article")
        article.set("name", name)
        article.text = text
    def set_article_text(self, name, text):
        for article in self.root:
            if article.get("name") == name:
                article.text = text
                break
    def get_article(self, name):
        for article in self.root:
            if article.get("name") == name:
                return [name, article.text]
    def findByText(self, text):
        arr = []
        for article in self.root:
            if article.text.find(text):
                arr.append([article.get("name"), article.text])
        return arr
    def findByName(self, name):
        arr = []
        for article in self.root:
            if article.get("name").find(name):
                arr.append([article.get("name"), article.text])
        return arr
        