from scrapy.contrib.spiders import XMLFeedSpider
from news.items import newsItem

import MySQLdb

#import database connection
db = MySQLdb.connect("localhost","root","local","MyDB")

#prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select url from MyDB.SourceUrls where deleted_ind is null limit 10"
arr = []

try:
	cursor.execute(sql)
	result = cursor.fetchall()
	#print result
	for row in result:
		arr.extend(row)	
except:
	print "Error: unable to fetch the data"

db.close()

#use XmlPathSelector (other one is HtmlXPathSelector - for HTML data)
class spider1(XMLFeedSpider):
	name='newsspider'
	#start_urls = ['http://feeds.mercurynews.com/mngi/rss/CustomR']
	start_urls = arr
	itertag = 'item'
	
	def parse_node(self, response, node):
		item = newsItem()
		if node is None :
			return None
		#extract() - returns a unicode string with the data selected by the XPath selector.
		item['title'] = node.select('title').extract()
		item['desc'] = node.select('description').extract()
		item['link'] = node.select('link').extract()
		return item

