from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    context['indexClass'] = 'active'
    return render(request,"index.html", context = context)

def about(request):
    context = {}
    context['aboutClass'] = 'active'
    return render(request,"about.html", context = context)

def blogDetails(request):
    context = {}
    context['indexClass'] = 'active'
    return render(request,"blog-details.html", context = context)

def blog(request):
    context = {}
    context['blogClass'] = 'active'
    return render(request,"blog.html", context = context)

def contact(request):
    context = {}
    context['contactClass'] = 'active'
    return render(request,"contact.html", context = context)

def portfolioDetails(request):
    context = {}
    context['indexClass'] = 'active'
    return render(request,"portfolio-details.html", context = context)

def portfolio(request):
    context = {}
    context['portfolioClass'] = 'active'
    return render(request,"portfolio.html", context = context)

def pricing(request):
    context = {}
    context['pricingClass'] = 'active'
    return render(request,"pricing.html", context = context)

def services(request):
    context = {}
    context['servicesClass'] = 'active'
    return render(request,"services.html", context = context)

def team(request):
    context = {}
    context['teamClass'] = 'active'
    return render(request,"team.html", context = context)

def testimonials(request):
    context = {}
    context['indexClass'] = 'active'
    return render(request,"testimonials.html", context = context)