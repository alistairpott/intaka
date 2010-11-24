from articles.factory import ArticleFactory


#get the input article list
fin = open('articles.txt','r')
article_list = fin.readlines()
fin.close()

#this class is used to build the article objects using source to choose a class
factory = ArticleFactory()


#source = ''
for line in article_list:
    #lines starting with '*' change the current article source
    if line[0] == '*':
        source = line[1:].strip()
    
    #if not then this is an article to be downloaded
    else: 
        #create an article object
        article_object = factory.buildArticle(source=source, url=line.strip())
        #tell the article to do it's work
        article_object.processArticle()
        #use the output from the article
        print article_object.getOutputHTML()