import articles.sources

def get_source_from_url(url):
    if url[:30] == 'http://moreintelligentlife.com':
        return 'IntelligentLife'
    elif url[:26] == 'http://www.economist.com':
        return 'Economist'
    
    return 'Economist'


class ArticleFactory:
    
    #build an article object using the source and url provided
    #source will decide which specific article class is used
    def buildArticle(self, url):
        #use the url to find the source of the article
        source = get_source_from_url(url)
        
        #get the appropriate article class using the source and naming convention
        article_class = getattr(articles.sources, '%sArticle' % source)
        
        #instantiate and return the article object
        return article_class(source, url)
        