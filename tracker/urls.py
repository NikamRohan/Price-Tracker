from django.urls import path
from . views import OrderListView,OrderDetailView,OrderCreateView
from . import views

urlpatterns = [
	path('',views.home,name = "home-page"),
    path('order_list', OrderListView.as_view(),name='tracker-home'),
    path('order/<int:pk>',OrderDetailView.as_view(),name='order-detail'),
    path('order/new/',OrderCreateView.as_view(),name='order-create'),
    path('about',views.about,name='tracker-about'),
]
