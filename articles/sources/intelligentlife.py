from base import BaseArticle
from BeautifulSoup import BeautifulSoup
import urllib2
from imagetag import ImageTag

class IntelligentLifeArticle(BaseArticle):
    
    def getPrintURL(self):
        #gonna grab from the normal page - don't bother with print
        print '\n  ->  Downloading an article...'
        print '  ->  Finding the print URL'
        pageText = urllib2.urlopen(self.url).read()
        soup = BeautifulSoup(pageText)
        self.printurl = 'http://moreintelligentlife.com' + soup.find('a', attrs={'class':'print-page print'})['href']
        return self.printurl
        
    def downloadArticle(self):
        print '  ->  Downloading the article...'
        #download the article and create a beautifulsoup object with it
        print '   *  ' + str(self.printurl)
        pageText = urllib2.urlopen(self.printurl).read()
        
        self.soup = BeautifulSoup(pageText)
    
    
    def extractData(self):
        self.title = ''
        self.headline = self.soup.find('h1',attrs={'class':'print-title'}).string
        self.rubric = ''
        
        #now do the body processing
        self.body = self.soup.find('div', attrs={'class':'print-content'})
        
        #remove empty and rubbish elements from the end of the body
        for element in self.body.contents[-5:]:
            element.extract()
        #this is the stupid paginfilter paragraph
        self.body.contents[1].extract()
        
        #download the images
        for element in self.body.findAll('img'):
            #skip past the spacer
            src = element['src']
            if src[-10:] != 'spacer.gif':
                imgtag = ImageTag('http://moreintelligentlife.com', element['src'])
                imgtag.downloadImage()
                #update the image tag to point at the downloaded file
                element.replaceWith(imgtag.getImageTagString())
            else:
                element.extract()
        