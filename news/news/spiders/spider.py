from scrapy.contrib.spiders import XMLFeedSpider
from news.items import newsItem

import MySQLdb

#import database connection
db = MySQLdb.connect("localhost","root","local","MyDB")

#prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select select url from sourceurls where deleted_ind is null limit 10"
arr = []

try:
	cursor.execute(sql)
	result = cursor.fetchall()
	print result
	for row in result:
		arr.append(row)	
except:
	print "Error: unable to fetch the data"

db.close()

spider1(XMLFeedSpider):
	name='newsspider'
	start_urls = ['http://feeds.mercurynews.com/mngi/rss/CustomR']
	itertag = 'item'
	
	def parse_node(self, response, node):
		item = newsItem()
		if node is None :
			return None
		item['title'] = node.select('title').extract()
		item['desc'] = node.select('description').extract()
		item['link'] = node.select('link').extract()
		return item

