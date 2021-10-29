from django.shortcuts import render
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerialiser
from django.http import HttpResponse
import json
# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerialiser

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Products.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)