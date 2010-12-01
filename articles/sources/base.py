import urllib
import urllib2

#the base article class that must be subclassed by the other types
class BaseArticle:
    
    def __init__(self, source, url):
        self.source = source
        self.url = url
    
    #go throught the basic steps required to download and process an article. normally basic but can change
    def processArticle(self):
        self.getPrintURL()
        self.downloadArticle()
        self.extractData()
    
    def getPrintURL(self):
        self.print_url = self.url
        return self.print_url
    
    def downloadArticle(self):
        print 'Program called the BASE download function'
        return 'Not implemented - you must subclass'
    
    def extractData(self):
        print 'Program called the BASE extract function'
        return 'Not implemented - you must subclass'
    
    #generate output HTML
    def getOutputHTML(self):
        output = ''
        if len(self.title) > 1:
            output += '<h4>' + str(self.title) + '</h4>'
        if len(self.headline) > 1:
            output += '<h2>' + str(self.headline) + '</h2>'
        if len(self.rubric) > 1:
            output += '<h5>' + str(self.rubric) + '</h5>'
        
        #get each element in the body
        for element in self.body:
            output += unicode(element)
        
        self.outputHTML = output
        #there are often unicode characters - so encode them using utf-8
        return unicode(output).encode('utf-8')