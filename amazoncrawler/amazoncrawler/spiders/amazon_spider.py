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
			# self.product_object=kwargs.get('order_object')
			# print(self.product_object)
			# print("11111111111111111111")
			# print(type(self.product_object))
			# self.url = self.product_object.url
			self.url = kwargs.get('url')
			self.desired_amount = kwargs.get('price_d')
			self.p_name = kwargs.get('name_p')
			self.mail_user = kwargs.get('u_mail')
			self.start_urls=[self.url]
			print("11111111111111111111111111111111111111111111111111111111111111111111111")

		else:
			self.check=0
			print("2222222222222222222222")
			self.url = kwargs.get('url')
			self.d_price = kwargs.get('d_price')
			self.start_urls=[self.url]
			self.author=kwargs.get('author')
			print(self.d_price)
			print(self.start_urls)
			print(self.author)
			# return scrapy.Request(self.start_urls[0],callback=self.parse)
				

	def parse(self, response):
		print("-11111-1-1--1-1--1-")
		if self.check==0:
			items = AmazoncrawlerItem()
			print("33333333333333333333")

			product_name = response.xpath("//div[@class='_3Z5yZS NDB7oB _12iFZG _3PG6Wd']/div[@class='ooJZfD _3FGKd2']/div[2]/div[@class='_3gijNv col-12-12']/div[@class='_29OxBi']/div/h1/span/text()")[0].extract()
			# print(product_name)
			product_price = response.xpath("//div[@class='_3Z5yZS NDB7oB _12iFZG _3PG6Wd']/div[@class='ooJZfD _3FGKd2']/div[2]/div[@class='_3gijNv col-12-12']/div[@class='_29OxBi']/div[@class='_3iZgFn']/div[@class='_2i1QSc']/div[@class='_1uv9Cb']/div[@class='_1vC4OE _3qQ9m1']/text()")[0].extract()
			s = response.xpath("//div[@class='_3Z5yZS NDB7oB _12iFZG _3PG6Wd']/div[@class='ooJZfD _3FGKd2']/div[@class='ooJZfD _2oZ8XT col-5-12 _2GJ0F-']/div/div/div/div[@class='keS6DZ']/div/div/ul/li/div/div/@style")[0].extract()
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

			product_price = response.xpath("//div[@class='_3Z5yZS NDB7oB _12iFZG _3PG6Wd']/div[@class='ooJZfD _3FGKd2']/div[2]/div[@class='_3gijNv col-12-12']/div[@class='_29OxBi']/div[@class='_3iZgFn']/div[@class='_2i1QSc']/div[@class='_1uv9Cb']/div[@class='_1vC4OE _3qQ9m1']/text()")[0].extract()
			print("Checking price")
			product_price = product_price.replace(",","")
			product_price = product_price[1:]
			# print(product_price,self.desired_amount)
			if int(product_price)<=int(self.desired_amount):
				subject='PRICE DROPPED!!!'
				print("Price Dropped")
				message= self.p_name + 'the product that you had set to track.Its Price dropped'
				email_from=settings.EMAIL_HOST_USER
				recipient_list = [self.mail_user]
				send_mail(subject, message, email_from, recipient_list,fail_silently=False)
				