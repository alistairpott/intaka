from base import BaseArticle
from BeautifulSoup import BeautifulSoup


class IntelligentLifeArticle(BaseArticle):
        
    def downloadArticle(self):
        fin = open('il-example.txt','r')
        data = fin.read()
        fin.close()
        self.soup = BeautifulSoup(data)
    
    def extractData(self):
        self.title = ''
        self.headline = self.soup.find('h1', attrs={'class':'print-title'}).string
        self.rubric = ''
        
        #now do the body processing
        self.body = self.soup.find('div', attrs={'class':'print-content'})
        
        #remove empty and rubbish elements from the end of the body
        for element in self.body.contents[-5:]:
			element.extract()
        
        #download and convert the images
        