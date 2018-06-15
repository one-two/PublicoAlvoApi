from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, request, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.

class BucketlistDetail(APIView):
    def get_object(self, pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bucketlist = self.get_object(pk)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BucketlistList(APIView):
    """
    List all Bucketlists, or create a new Bucketlist.
    """
    def get(self, request, format=None):
        Bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(Bucketlists, many=True)
        #print(serializer.data[1]['name'])
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    pass