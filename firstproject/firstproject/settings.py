# Scrapy settings for firstproject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'firstproject'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['firstproject.spiders']
NEWSPIDER_MODULE = 'firstproject.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

