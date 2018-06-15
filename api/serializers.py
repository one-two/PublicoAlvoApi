from rest_framework import serializers
from .models import Bucketlist, User

class BucketlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified', 'user')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'secret')