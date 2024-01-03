from django.shortcuts import render
#from django.http import HttpResponse
from .models import Article
from .serializers import ArticleSerializers
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializers
    

    
    
    
    
    
# def hello(request):
#     return HttpResponse('Hello world !!!')

# def about(request):
#     return HttpResponse('This is my first django application.')