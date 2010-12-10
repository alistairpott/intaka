from base import BaseArticle
from imagetag import ImageTag
import urllib2
from BeautifulSoup import BeautifulSoup


class EconomistArticle(BaseArticle):
    
    def __init__(self, source, url):
        BaseArticle.__init__(self,source, url)
        self.getArticleType()
        
    
    #use the URL to figure out what kind of article this is
    def getArticleType(self):
        if self.url.find('node') > 0:
            self.article_type = 'node'
        elif self.url.find('blogs') > 0:
            self.article_type = 'blog'
        elif self.url.find('cfm') > 0:
            self.article_type = 'cfm'
    
    #get the URL of the print page for this article    
    def getPrintURL(self):
        if self.article_type in ['node','blog']:
            return self.url + '/print'
        else:
            return 'http://www.economist.com/node/' + self.url[self.url.rfind('=') + 1:] + '/print'
    
    #actually download the article text
    def downloadArticle(self):
        print '\n  ->  Downloading an article...'
        print '   *  ' + str(self.url)
        
        #download the article and create a beautifulsoup object with it
        pageText = urllib2.urlopen(self.getPrintURL()).read()
        
        if self.article_type in ['node','cfm']:
            self.soup = BeautifulSoup(pageText).find('div', id='ec-article-body')
        else:
            self.soup = BeautifulSoup(pageText)
    
    
    #process the body of the article
    def extractData(self):
        if self.article_type in ['node','cfm']:
            self.title = unicode(self.soup.find('h1').string.strip())
            self.headline = unicode(self.soup.find('div', attrs={'class':'headline'}).string.strip())
            self.rubric = unicode(self.soup.find('h2', attrs={'class':'rubric'}).string.strip())
            
        elif self.article_type == 'blog':
            self.title = unicode(self.soup.find('h2', attrs={'class':'ec-blog-fly-title'}).string.strip())
            self.headline = unicode(self.soup.find('p', attrs={'class':'ec-blog-headline'}).string.strip()) 
            self.rubric = unicode('') 

        #extract the body of the article
        if self.article_type in ['node','cfm']:
            self.body = self.soup.find('div', attrs={'class':'ec-article-content clear'})
        elif self.article_type == 'blog':
            self.body = self.soup.find('div', attrs={'class':'ec-blog-body'})
        
        #download the images
        for element in self.body.findAll('img'):
            imgtag = ImageTag('http://www.economist.com', element['src'])
            imgtag.downloadImage()
            #update the image tag to point at the downloaded file
            element.replaceWith(imgtag.getImageTagString())
        
        #remove the related items divs
        for element in self.body.findAll('div', {'class':'related-items'}):
            element.extract()