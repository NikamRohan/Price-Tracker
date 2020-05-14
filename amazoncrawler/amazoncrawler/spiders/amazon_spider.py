import scrapy
from ..items import AmazoncrawlerItem
from tracker.models import Order
from amazoncrawler.spiders import amazon_spider
from amazoncrawler import pipelines

from django.core.mail import send_mail
from django.conf import settings

class AmazonSpider(scrapy.Spider):
	name = "amazon"
	start_urls = [
	'123']
	print("1111")

	def __init__(self, *args,**kwargs):
		# super(AmazonSpider, self).__init__(*args, **kwargs)
		if kwargs.get('check'):
			self.check=1
			self.product_object=kwargs.get('order_object')
			self.url = self.product_object.url
			self.start_urls=[self.url]
			print("11111111111111111111111111111111111111111111111111111111111111111111111")

		else:
			self.check=0
			# print("2222222222222222222222")
			self.url = kwargs.get('url')
			self.d_price = kwargs.get('d_price')
			self.start_urls=[self.url]
			self.author=kwargs.get('author')
			# return scrapy.Request(self.start_urls[0],callback=self.parse)
				

	def parse(self, response):
		# print("-11111-1-1--1-1--1-")
		if self.check==0:
			items = AmazoncrawlerItem()
			# print("33333333333333333333")

			product_name = response.xpath("//div[@class='t-0M7P _3GgMx1 _2doH3V']/div[@class='_3e7xtJ']/div[@class='_1HmYoV hCUpcT']/div[@class='_1HmYoV _35HD7C col-8-12']/div[@class='bhgxx2 col-12-12']/div[@class='_29OxBi']/div/h1/span/text()")[0].extract()
			product_price = response.xpath("//div[@class='t-0M7P _3GgMx1 _2doH3V']/div[@class='_3e7xtJ']/div[@class='_1HmYoV hCUpcT']/div[@class='_1HmYoV _35HD7C col-8-12']/div [@class='bhgxx2 col-12-12']/div[@class='_29OxBi']/div[@class='_3iZgFn']/div[@class='_2i1QSc']/div/div[@class='_1vC4OE _3qQ9m1']/text()")[0].extract()
			s = response.xpath("//div[@class='t-0M7P _3GgMx1 _2doH3V']/div[@class='_3e7xtJ']/div/div/div/div/div/div/div/div/ul/li/div/div/@style")[0].extract()
			l = s.split('(')
			product_img = l[1][:-1]
			print(product_name)
			print(product_img)
			items['product_name'] = product_name
			items['price'] = product_price
			items['image'] = product_img
			items['author'] = self.author
			items['desired_price'] = self.d_price
			items['url'] =  self.url
			#TO EXPLICITLY CALL PIPELINE
			obj = pipelines.AmazoncrawlerPipeline()
			obj.process_item(items,'amazon')
			# print("111111111111111111111111")
			print(items)
			yield items

		else:

			product_price = response.xpath("//div[@class='t-0M7P _3GgMx1 _2doH3V']/div[@class='_3e7xtJ']/div[@class='_1HmYoV hCUpcT']/div[@class='_1HmYoV _35HD7C col-8-12']/div [@class='bhgxx2 col-12-12']/div[@class='_29OxBi']/div[@class='_3iZgFn']/div[@class='_2i1QSc']/div/div[@class='_1vC4OE _3qQ9m1']/text()")[0].extract()
			print("Checking price")
			if product_price<=self.desired_price:
				subject='PRICE DROPPED!!!'
				message= self.product_name + 'the product that you had set to track.Its Price dropped'
				email_from=settings.EMAIL_HOST_USER
				recipient_list = ['rohananilnikam1999@gmail.com',]
				send_mail(subject, message, email_from, recipient_list,fail_silently=False)