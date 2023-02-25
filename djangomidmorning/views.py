from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to DJANGO Class")
def emobilis(request):
    return HttpResponse('eMobilis tech institute')
def harambee(request):
    return HttpResponse("it is based on african socialism")
def hairstyles(request):
    return HttpResponse("box braids are the cheapest of all")
def movies(request):
    return HttpResponse("Our kinds of people is based on the history of single mothers")