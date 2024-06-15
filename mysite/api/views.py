from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import blogPost
from .serializers import blogPostSerializer

class blogPostListCreate(generics.ListCreateAPIView):
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer
    
    def delete(self,request,*args, **kwargs):
        blogPost.objects.all().delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class blogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer
    lookup_field = 'pk'