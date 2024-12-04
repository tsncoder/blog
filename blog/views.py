from django.http import HttpResponse
from django.shortcuts import render
from .db_articles import articles

def home_view(request):
    # return HttpResponse('hello stephane encore')
    return render(request, 'home.html')
def contact_view(request):
    # return HttpResponse('contactez nous')
    return render(request, 'contact.html')
def article_view(request):
    # return HttpResponse('contactez nous')
    return render(request, 'article.html', context={'articles': articles})