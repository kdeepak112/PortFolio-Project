from django.shortcuts import render
from .models import contactRequest
from django.utils.html import escape
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from datetime import datetime
import asyncio
from django.core.mail import EmailMessage
from django.conf import settings  
from django.template.loader import render_to_string
import asyncio
import os 

BASE_DIR = settings.BASE_DIR
# Create your views here.
def index(request):
    context = {}
    context['indexClass'] = 'active'
    return render(request,"index.html", context = context)

def about(request):
    context = {}
    context['aboutClass'] = 'active'
    return render(request,"about.html", context = context)


def contact(request):
    context = {}
    context['contactClass'] = 'active'

    if request.method == "POST":
        name = escape(request.POST['name'])
        email = escape(request.POST['email'])
        subject = escape(request.POST['subject'])
        message = escape(request.POST['message'])

        try:
            validate_email(email)
            
            contactObj = contactRequest()
            contactObj.name = name
            contactObj.email = email
            contactObj.subject = subject
            contactObj.message = message
            contactObj.requested_on = datetime.now()
            contactObj.save()

            context['statusCode'] = 200
            context['desc'] = "Request Captured Successfully"

            # Send email asynchronously
            recipient_list = ["dkumardk002@gmail.com"]
            subject = "You Have Reached Us..!!"
            sendContactEmail(subject, recipient_list)

        except ValidationError:
            context['statusCode'] = 500
            context['desc'] = "Invalid Email submitted"
    print(context)
    return render(request,"contact.html", context = context)

def portfolioDetails(request):
    context = {}
    context['indexClass'] = 'active'
    return render(request,"portfolio-details.html", context = context)

def portfolio(request):
    context = {}
    context['portfolioClass'] = 'active'
    return render(request,"portfolio.html", context = context)



# Define the async function to send the email
def sendContactEmail(subject, receipientList):
    fromEmail = settings.EMAIL_HOST_USER

    current_year = datetime.now().year 
    htmlContent = render_to_string(os.path.join(BASE_DIR,'template','contact_email.html'), {'current_year': current_year})

    email = EmailMessage(
        subject=subject,
        body=htmlContent,
        from_email=fromEmail,
        to=receipientList,
    )
    email.content_subtype = 'html'
    email.send()
  # Send the email in a non-blocking way
