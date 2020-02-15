from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Author, Details


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'description', 'state']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'cellphone', 'post', 'state']


class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ['url', 'reference', 'author', 'post', 'state']
