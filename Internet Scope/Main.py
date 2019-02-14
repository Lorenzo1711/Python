"""
parsePy
"""
from bs4 import BeautifulSoup
import lxml
from urllib.request import urlopen, Request

className = "discount_original_price"
def parse(url, tagToFind, classToFind):
	"""
	Parse a URL for a given tag with a given class.
	Returns either a string or a list depending on how many elements
	of that type and class name there were
    Keyword arguments:
    url -- the url that needs to be parsed
	tagToFind -- The tag that is searched for
	classToFind -- The class that the tagToFind must have
    """
	url_to_use = url
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(url_to_use, headers=hdr)
	html = urlopen(req)
	bsObj = BeautifulSoup(html.read(), 'lxml')
	x = [url.string for url in bsObj.find_all(tagToFind, {"class": classToFind})]
	return x 

def parse_url_array(urls, tagToFind, classToFind):
	"""
	Parses an array of URLS for a tag of a given class. Returns either a 1d or 2d list
	
	urls -- A list of URLS to search
	tagToFind -- The tag to be searched for
	classToFind -- The class that the tagToFind must have in order to be returned
	"""
	results= []
	
	for url in urls:
		url_to_use = url
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = Request(url_to_use, headers=hdr)
		html = urlopen(req)
		bsObj = BeautifulSoup(html.read(), 'lxml')
		x = [url.string for url in bsObj.find_all(tagToFind, {"class": classToFind})]
		results.append(x)
	return results
"""
def generateSequentialUrls(baseURL, lowerLimit = 0, upperLimit, writeToFile = False):
	
	Generates a set of sequential URLS
	baseURL -- what the number should be appended to 
	lowerLimit -- The smallest number that should be appended (by default 0)
	upperLimit -- The largest number that should be appended 
	writeToFile -- Should the result be written to a file once complete
	
	urlList = []
	for i in range(lowerLimit, upperLimit):
		urlList.append(baseURL + i)
	
	if writeToFile:
		f = open(baseURL + ".list", "w")
		for url in urlList:
			f.write(url + "\n")
		f.close()
		print("SUCCESS")
		print("The file can be found at\n" + baseURL + ".list")
		
	return urlList
	"""
#More will be added, this is just my lazy way to reuse code
parse(https://www.bbc.co.uk/weather/0/2643743, )
