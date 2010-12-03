class DocBuilder:
    """A class for construcing documents ready to be converted to ebooks."""
    
    def __init__(self, title, filename='output'):
        """Setup the document builder using input parameters
        
            title    = The title out the output document
            filename = Optional filename of the output document. Defaults to output
        """
        self.title = title
        self.filename = filename
        self.has_toc = False
        self.has_cover = False
        
        #list to hold all the articles in the document
        self.articles = []
    
    def output_all_files(self):
        """Goes through the steps to create the output files."""
        self.buildTableOfContents()
        self.buildOPF()
        self.buildOutput()
    
    def set_cover(self, cover_filename):
        """Sets the cover of the output document"""        
        self.cover_filename = cover_filename
        self.has_cover = True
    
    def add_article(self, html, toc_label):
        """Adds an article to the DocBuilder.
            
            html      = the HTML content of the article
            toc_label = the label of this article in the Table of Contents
        """        
        #create an anchor automatically
        toc_anchor = 'anchor%i' % len(self.articles)
        
        self.articles.append({'toc_label':toc_label, 'toc_anchor':toc_anchor, 'html':html})
    
    def buildTableOfContents(self, title='Table of Contents'):
        """Outputs the Table of Contents to a file"""
        fout = open('toc.html','w')
        fout.write('<h1>%s</h1>' % title)
        
        #actually write the output file
        for item in self.articles:
            fout.write('<p><a href="%s.html#%s">%s</a></p>' % (self.filename, item['toc_anchor'], item['toc_label']))
        
        self.has_toc = True
        fout.close()
    
    def buildOPF(self):
        """Builds the output OPF file."""
        #get the template for the OPF
        fin = open('template.opf','r')
        opf_output = fin.read()
        fin.close()
        
        #update the placeholders in the template
        opf_output = opf_output.replace('{TITLE}', self.title)
        opf_output = opf_output.replace('{FILENAME}', self.filename)
        if self.has_cover:
            opf_output = opf_output.replace('{COVER}', '<EmbeddedCover>%s</EmbeddedCover>' % self.cover_filename)
        else:
            opf_output = opf_output.replace('{COVER}', '')
        
        #write the output file
        fout = open('%s.opf' % self.filename, 'w')
        fout.write(opf_output)
        fout.close()
    
    def buildOutput(self):
        """Builds the output HTML file with the document contents."""
        fout = open('%s.html' % self.filename, 'w')
        fout.write('<html><head><title>Economist Download</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>')
        for item in self.articles:
            fout.write('<a name="%s"></a>' % item['toc_anchor'])
            fout.write(item['html'])
            fout.write('<mbp:pagebreak/>')
        fout.write('</body></html>')
        fout.close()
        
