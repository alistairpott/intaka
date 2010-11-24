import articles.sources

class ArticleFactory:
    
    #build an article object using the source and url provided
    #source will decide which specific article class is used
    def buildArticle(self, source, url):
        
        #get the appropriate article class using the source and naming convention
        article_class = getattr(articles.sources, source + 'Article')
        
        #instantiate and return the article object
        return article_class(source, url)
        