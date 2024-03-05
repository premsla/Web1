from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_view(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def my_first_view(request):
    template = loader.get_template('my_first.html')
    return HttpResponse(template.render())
def Bevarage_views(request):
    template = loader.get_template('Beverage.html')
    return HttpResponse(template.render())
def Beauty_views(request):
    template = loader.get_template('beauty.html')
    return HttpResponse(template.render())
def Fashion_views(request):
    template = loader.get_template('Fashion.html')
    return HttpResponse(template.render())
def Accessories_views(request):
    template = loader.get_template('accessories.html')
    return HttpResponse(template.render())
def Personal_care_views(request):
    template = loader.get_template('personalcare.html')
    return HttpResponse(template.render())
def kids_views(request):
    template = loader.get_template('kids.html')
    return HttpResponse(template.render())
def Men_views(request):
    template = loader.get_template('men.html')
    return HttpResponse(template.render())
def all_brands_views(request):
    template = loader.get_template('all_brands.html')
    return HttpResponse(template.render())
def cart_views(request):
    template = loader.get_template('cartPage.html')
    return HttpResponse(template.render())
def Eyes_views(request):
    template = loader.get_template('eyes.html')
    return HttpResponse(template.render())
def Face_views(request):
    template = loader.get_template('Face.html')
    return HttpResponse(template.render())
def Lips_views(request):
    template = loader.get_template('lips.html')
    return HttpResponse(template.render())