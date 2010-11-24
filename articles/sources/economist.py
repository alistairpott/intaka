from base import BaseArticle

class EconomistArticle(BaseArticle):
    def getOutputHTML(self):
        return self.source + ':' + self.url
        