from natgeo import NationalGeographicArticle

a = NationalGeographicArticle('NationalGeographic','http://')

a.processArticle()

print a.getOutputHTML()