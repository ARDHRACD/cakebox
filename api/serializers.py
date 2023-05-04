from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Cakes,Carts,Orders,Reviews

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields=["id","user","comment","rating"]
    
class CakeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    cake_review=ReviewSerializer(read_only=True,many=True)
    class Meta:
        model=Cakes
        fields=["id","cake_name","shape","cake","layers","image","weight","price","cake_review"]
    
class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["user","status","qty","created_date","cake"]

class OrderSerializer(serializers.ModelSerializer):
    cake=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_deliverydate=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=["cake","user","created_date","status","expected_deliverydate","address","matter"]
