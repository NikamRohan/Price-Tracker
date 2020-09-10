from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from tracker.models import Order
from tracker.views import OrderCreateView

from background_task import background




@background(schedule=5000)
def notify_user():
	print("!!!!!!!!!!!!!!!")
	order_set=Order.objects.all()
	print(order_set)

	for order in order_set:
		# my_url=order.url
		# obj=AmazonBot()
		# retrieved_price=obj.get_price_only(my_url)
		# print(type(order))
		# break
		# print(order.author.email)
		OrderCreateView.new_product(order,-1)
				



		# if retrieved_price<=order.desired_price:
		# 	subject='PRICE DROPPED!!!'
		# 	message= order.product_name + 'the product that you had set to track.Its Price dropped'
		# 	email_from=settings.EMAIL_HOST_USER
		# 	recipient_list = ['rohananilnikam1@gmail.com',]
		# 	send_mail(subject, message, email_from, recipient_list,fail_silently=False)
            



