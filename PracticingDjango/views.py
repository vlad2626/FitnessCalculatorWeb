from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(requests,*args, **kwargs):
    variables ={ "Name" :"Melanie",
                 "Last name":" Orozco",
                 "Middle":"Alexandra",
                 "Age":"25"
    }
    return render(requests, "home.html", variables)

