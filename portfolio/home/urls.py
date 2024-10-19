
from django.urls import path , include
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("blog-details/",blogDetails,name="blog-details"),
    path("blog/",blog,name="blog"),
    path("contact/",contact,name="contact"),
    path("portfolio-details/",portfolioDetails,name="portfolio-details"),
    path("portfolio/",portfolio,name="portfolio"),
    path("pricing/",pricing,name="pricing"),
    path("services/",services,name="services"),
    path("team/",team,name="team"),
    path("testimonials/",testimonials,name="home"),
]
