from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    game = serializers.ReadOnlyField(source='game.title')

    class Meta:
        model = Review
        fields = '__all__'

class UserLibrarySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    game = serializers.ReadOnlyField(source='game.title')

    class Meta:
        model = UserLibrary
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    game = serializers.ReadOnlyField(source='game.title')

    class Meta:
        model = Order
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    game = serializers.ReadOnlyField(source='game.title')

    class Meta:
        model = Wishlist
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'