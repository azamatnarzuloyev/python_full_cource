from django.shortcuts import  get_object_or_404
from .models import Worlds
from rest_framework import generics, response, status, views, permissions
from .serializers import WorldsSerializers
from .pagination import CustomPagination
from rest_framework import filters ,pagination

from rest_framework import generics
from django_filters import rest_framework as fil



class ProductFilter(fil.FilterSet):

    class Meta:
        model = Worlds
        fields = ["world", ]



class WorldListViews(generics.ListAPIView):
    serializer_class = WorldsSerializers
    queryset = Worlds.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["world"]
    lookup_field = "slug"
 
    filter_backends = (fil.DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = CustomPagination
    # search_fields = ('name', 'categories__name')
    # ordering_fields = ('name', 'categories__name')
   
    
    def get(self, request, *args, **kwargs):
        self.serializer_class = WorldsSerializers
        return super().get(request, *args, **kwargs)
      
  


class WorldDetailView(generics.RetrieveAPIView):
    serializer_class = WorldsSerializers
    queryset = Worlds.objects.all()
    lookup_field = "slug"
    filter_backends = (fil.DjangoFilterBackend,)
    filterset_class = ProductFilter
    
    
class WorldSearch(generics.ListAPIView):
    serializer_class = WorldsSerializers
    queryset = Worlds.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["world"]
    lookup_field = "slug"
