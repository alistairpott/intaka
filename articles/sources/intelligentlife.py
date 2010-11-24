from base import BaseArticle

class IntelligentLifeArticle(BaseArticle):
    def getOutputHTML(self):
        return self.source + ':' + self.url