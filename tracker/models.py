from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Order(models.Model):
	product_name=models.CharField(max_length=100)
	price= models.CharField(max_length=100)
	desired_price=models.CharField(max_length=100)
	date_posted=models.DateTimeField(default=timezone.now)
	url=models.CharField(max_length=500)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.URLField(null = True, blank = True)


	def __str__(self):
		return self.product_name


	def get_absolute_url(self):
		return reverse('tracker-home')