from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Order 
from django.views.generic import ListView,DetailView,CreateView

import time
from django.http import HttpResponseRedirect
from django.urls import reverse


#FOR SCRAPY

import os
import sys

sys.path.append("C:/Users/admin/Desktop/COLLEGE/Desktop/DJANGO/django_amazon/amazoncrawler")

from amazoncrawler.spiders import amazon_spider

from scrapy import signals
from twisted.internet import reactor
from scrapy.crawler import Crawler,CrawlerRunner
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

from amazoncrawler.pipelines import AmazoncrawlerPipeline
from amazoncrawler import settings as amazon_settings

from scrapy.utils.log import configure_logging
from crochet import setup

def home(request):
    return render(request, 'tracker/home_page.html')

def about(request):
    return render(request, 'tracker/about.html', {'title': 'About'})


class OrderListView(ListView): 
    # model = Order
    template_name='tracker/home.html'
    context_object_name='orders'
    ordering=['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        return Order.objects.filter(author = self.request.user) # lhs the field you want and rhs will be same self.request.user


class OrderDetailView(DetailView):
    model=Order


class OrderCreateView(LoginRequiredMixin,CreateView):
    model=Order
    fields=['url','desired_price']

    def form_valid(self,form):
        f = self.new_product(form)
        
        if f==1:
            messages.success(self.request, f'Product Added successfully! We will notify you via email when price drop under your desire price')
            return HttpResponseRedirect(reverse('tracker-home'))

    def new_product(self,form):
        setup()
        print(form)
        if form==-1:
            myurl = self.url

            settings = {
                'url' : myurl
            }

            def spider_closing(spider):
                """Activates on spider closed signal"""
                print("Spiderclose"*10)
            print(myurl)
            o_obj = self
            crawler = Crawler(amazon_spider.AmazonSpider,settings)
            # print(amazon_spider.AmazonSpider,settings)

            crawler.signals.connect(spider_closing, signal=signals.spider_closed)

            crawler.crawl(order_obj = o_obj,check=1)

            while True:
                time.sleep(1)
                #print(crawler.stats.get_stats())
                st = crawler.stats.get_stats()
                print(st)
                try:
                  fr=crawler.stats.get_stats()['finish_reason']
                  print(fr)
                  if fr=='finished':
                    break
                except:
                  pass

            # time.sleep(15)

        else:
            myurl = self.request.POST['url']
            d_price = self.request.POST['desired_price']

            print("!!!!!!!!!!!!!!!!!")
            settings = {
                            'url':myurl
                    }

            u=self.request.user

            crawler = Crawler(amazon_spider.AmazonSpider,settings)

            crawler.crawl(url=myurl,d_price=d_price,author=self.request.user,check=0)
            st = crawler.stats.get_stats()
            print(st)
            while True:
                print(crawler.stats.get_stats())
                time.sleep(1)
                #print(crawler.stats.get_stats())
                try:
                  fr=crawler.stats.get_stats()['finish_reason']
                  print(fr)
                  if fr=='finished':
                    break
                except:
                  pass
            
            return 1