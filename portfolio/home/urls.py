
from django.urls import path , include
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("myskills/",myskills,name="myskills"),
    path("contact/",contact,name="contact"),
    path("portfolio/",portfolio,name="portfolio"),
]
