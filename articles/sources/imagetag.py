import urllib

#for handling image tags in the input
class ImageTag:
	def __init__(self, url_prefix, imgurl):
		if imgurl[0:4] != 'http':
			self.original_url = url_prefix + imgurl
		else:
			self.original_url = imgurl
		
		self.genFileName()
		
	#generate a filename for the downloaded image
	def genFileName(self):
		ext = self.original_url[self.original_url.rfind('.') + 1:]
		self.filename = 'img/img_' + str(int(random.random()*100000)) + '.' + ext
	
	#download the image
	def downloadImage(self):
		print '   *  Downloading an image...'
		urllib.urlretrieve(self.original_url, self.filename)
	
	#return a string for the img tag
	def getImageTagString(self):
		return '<img src="' + self.filename + '">'
