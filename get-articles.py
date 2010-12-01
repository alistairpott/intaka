import os

from articles.factory import ArticleFactory
from docbuilder import DocBuilder

#get the input article list
fin = open('articles.txt','r')
article_list = fin.readlines()
fin.close()

#from now on we work in the output directory
os.chdir('output')

#this class is used to build the article objects using source to choose a class
factory = ArticleFactory()

#get the title for the output file
title = raw_input('Enter the title for the whole document: ')

#this collects all of the articles and then does the appropriate output
doc = DocBuilder(title)


for line in article_list:
    #lines starting with '*' change the current article source
    if line[0] == '*':
        source = line[1:].strip()
    
    #if not then this is an article to be downloaded
    else: 
        #create an article object
        article_object = factory.buildArticle(url=line.strip())
        #tell the article to do it's work
        article_object.processArticle()
        #use the output from the article
        doc.add_article(html = article_object.getOutputHTML(),
                        toc_label = article_object.title)

#now that all articles are downloaded build the output
doc.output_all_files()

#run the output through the kindlegen program