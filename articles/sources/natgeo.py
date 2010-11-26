from base import BaseArticle
from BeautifulSoup import BeautifulSoup


class NationalGeographicArticle(BaseArticle):
        
    def downloadArticle(self):
        fin = open('ng-example.txt','r')
        data = fin.read()
        fin.close()
        self.soup = BeautifulSoup(data)
    
    def extractData(self):
        self.title = ''
        self.headline = self.soup.find('div', attrs={'class':'printpage_title'}).string
        self.rubric = self.soup.find('div', attrs={'class':'printpage_subtitle'}).string
        
        #now do the body processing
        self.body = self.soup.find('div', attrs={'id':'printpage_contain'})
        
        #download and convert the images
        