#define your item pipelines here
from scrapy.exceptions import DropItem
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb

#import database connection
db = MySQLdb.connect("localhost","root","local","MyDB")

#prepare a cursor object using cursor() method
cursor = db.cursor()

class newsPipeline(object):
    def process_item(self, item, spider):		  
	for a in item['title']: 			# Pick each item from the list
 		a1=item.get('title')[0]		# Get the zero-index value for the 'title' key
            	a2=item.get('link')[0]		# Get the zero-index value for the 'link' key
           	a3=item.get('desc')[0]		# Get the zero-index value for the 'desc' key
            	b1=a1[7:-15]
           	b2=a2[6:-14]
            	b3=a3[13:-29]
            	del item['title']
            	item['title']=b1			# New edited title values assigned
            	item['link']=b2
           	item['desc']=b3
	filter = ['Japan', 'japan', 'Japanese', 'japanese', 'earthquake', 'Earthquake', 'tsunami', 'Tsunami'] 
	for x in filter:
		for s,t in item.iteritems():
			if x in s or x in t:
				#return item
				#prepare SQL query to insert record into database
				sql = "INSERT INTO MyDB.EventMap\
					(event_id,url_id,title,description,link,other,created_date,keyword)\
					VALUES\
					(1,1,'%s','%s','%s',null,null,null)"%(item['title'],item['desc'],item['link'])
				try:
					#Execute the sql command
					cursor.execute(sql)
					#commit your chnages in database
					db.commit()
					#print sql
				except:
					#rollback in case of any error
					db.rollback()
					print 'error'
			else: 
				raise DropItem ("Not correct")
	#disconnect from the server
	db.close()
'''
class WsjPipeline(object):
	def process_item(self, item, spider):
		a1 = item.get('title')[1]
		a2 = item.get('link')[1]
		a3 = item.get('desc')[1]
		for t in item.iteritems():
			b1=a1[7:-15]
			b2=a2[6:-14]
			b3=a3[13:-29]
			del item['title']
			item['title']=b1
			item['link']=b2
			item['desc']=b3
		return item
class WsjPipeline2(object):
	def process_item(self, item, spider):
		for a in item['title']:
			a1 = item.get('title')
			a2 = item.get('link')
			a3 = item.get('desc')
			for t in item.iteritems():
				b1 = a1 + 'tuvalabs'
				b2 = a2
				b3 = a3
				del item['title']
				ite['title']=b1
			return item
'''
