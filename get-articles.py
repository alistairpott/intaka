import os

from articles.factory import ArticleFactory
from docbuilder import DocBuilder

#get the input article list
fin = open('articles.txt','r')
article_list = fin.readlines()
fin.close()

#from now on we work in the output directory
os.chdir('output')
#remove any old pictures that are in the output images folder
folder = 'img'
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    os.unlink(filepath)

#this class is used to build the article objects using source to choose a class
factory = ArticleFactory()

#get the title for the output file
title = raw_input('Enter the title for the whole document: ')

#this collects all of the articles and then does the appropriate output
doc = DocBuilder(title)

for line in article_list:
    #create an article object
    article_object = factory.buildArticle(url=line.strip())
    #tell the article to do it's work
    article_object.processArticle()
    #use the output from the article
    doc.add_article(html      = article_object.getOutputHTML(),
                    toc_label = article_object.title)

#now that all articles are downloaded build the output
doc.output_all_files()

#run the output through the kindlegen program