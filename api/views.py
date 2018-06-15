from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, request, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist, User

# Create your views here.

# Poll.objects.get(
#     Q(question__startswith='Who'),
#     Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
# )

class BucketlistDetail(APIView):
    def get(self, request, pk, format=None):
        bucketlist = Bucketlist.objects.filter(pk=pk)#self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist, many=True)
        #print(serializer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bucketlist = Bucketlist.objects.get(pk=pk)
        serializer = BucketlistSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bucketlist = Bucketlist.objects.get(pk=pk)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BucketlistList(APIView):
    """
    List all Bucketlists, or create a new Bucketlist.
    """
    def get(self, request, format=None):
        Bucketlists = Bucketlist.objects.all().select_related('user')
        serializer = BucketlistSerializer(Bucketlists, many=True)
        for u in serializer.data:
            qq = u['user']
            oi = User.objects.filter(pk__exact=qq)
            print(oi)
            print(u['user'])
            #u['user'] = UserSerializer(User.objects.get(pk=u['user']))
        #print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request, format=None):
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        #print(serializer.data[1]['name'])
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListDetail(APIView):
    def get(self, request, pk, format=None):
        user = User.objects.filter(pk__exact=pk)#self.get_object(pk)
        serializer = UserSerializer(user, many=True)
        #print(serializer)
        return Response(serializer.data)