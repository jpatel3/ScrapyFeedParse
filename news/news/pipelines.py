#define your item pipelines here
from scrapy.exceptions import DropItem
from xml.dom.minidom import parseString
#import xml.parser.expat
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb

#import database connection
db = MySQLdb.connect("localhost","root","local","MyDB")

#prepare a cursor object using cursor() method
cursor = db.cursor()

class newsPipeline(object):
    def process_item(self, xmlitem, spider):
	print 'xmlitem: ', xmlitem	
	item = {}  
	for a in xmlitem['title']: 			# Pick each item from the list
		item['title'] = parseString(xmlitem.get('title')[0]).firstChild.firstChild.toxml()
		item['link'] = parseString(xmlitem.get('link')[0]).firstChild.firstChild.toxml()
		item['desc'] = parseString(xmlitem.get('desc')[0]).firstChild.firstChild.toxml()
		#print 'a1 :', item['title'], 'a2 :', item['link'], 'a3 :', item['desc']
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
