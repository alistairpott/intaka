
#a class for building the output files OPF, TOC, MAIN, COVER, etc
class DocBuilder:

    def __init__(self, title, filename='output'):
        #basic params on creating the document
        self.title = title
        self.filename = filename
        self.has_toc = False
        self.has_cover = False
        
        #list to hold all the articles in the document
        self.articles = []
    
    #utility function to create all of the output files
    def output_all_files(self):
        self.buildTableOfContents()
        self.buildOPF()
        self.buildOutput()
    
    #set the cover for the document
    def set_cover(self, cover_filename):
        self.cover_filename = cover_filename
        self.has_cover = True
    
    #add an article to the document
    def add_article(self, html, toc_label, toc_anchor='AUTO'):
        #create an anchor automatically
        if toc_anchor == 'AUTO':
            toc_anchor = 'anchor%i' % len(self.articles)
        
        self.articles.append({'toc_label':toc_label, 'toc_anchor':toc_anchor, 'html':html})
    
    #write a table of contents file
    def buildTableOfContents(self, title='Table of Contents'):
        fout = open('toc.html','w')
        fout.write('<h1>%s</h1>' % title)
        
        #actually write the output file
        for item in self.articles:
            fout.write('<p><a href="%s.html#%s">%s</a></p>' % (self.filename, item['toc_anchor'], item['toc_label']))
        
        self.has_toc = True
        fout.close()
    
    #build the output OPF file
    def buildOPF(self):
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
    
    #build the main output file
    def buildOutput(self):
        fout = open('%s.html' % self.filename, 'w')
        for item in self.articles:
            fout.write('<a name="%s"></a>' % item['toc_anchor'])
            fout.write(item['html'])
        fout.close()
        
