# Here we basically deffine the functions either by class also
from django.http import HttpResponse


def home_page(request):
    print("hello to all")
    return HttpResponse("this is new page")