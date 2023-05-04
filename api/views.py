from django.shortcuts import render
from api.models import Cakes,Carts,Orders,Reviews
from rest_framework.viewsets import ModelViewSet,ViewSet,GenericViewSet
from rest_framework.response import Response
from api.serializers import  UserSerializer,CakeSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.decorators import action

# Create your views here.

class UserView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class CakeView(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    serializer_class=CakeSerializer
    queryset=Cakes.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=Cakes.objects.all()

        if "layers" in self.request.query_params:
            lay=self.request.query_params.get("layers")
            qs=qs.filter(layers=lay)

        if "shape" in self.request.query_params:
            shp=self.request.query_params.get("shape")
            qs=qs.filter(shape=shp)
        return qs
    
    @action(methods=["post"],detail=True)
    def addto_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            # qs=Carts.objects.create(cake=cake,user=request.user,qty=serializer.validated_data.get("quantity"))
            # serializer=CartSerializer(qs)
            serializer.save(cake=cake,user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    @action(methods=["post"],detail=True)
    def make_order(self,request,*args,**kwargs):
        cake=self.get_object()
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cake=cake,user=request.user)
            # qs=Orders.objects.create(cake=cake,
            #                         user=request.user,
            #                         address=serializer.validated_data.get("address"),
            #                         matter=serializer.validated_data.get("matter"),

            #                         )
            # serializer=OrderSerializer(qs)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cake=cake,user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# localhost:8000/api/products/1/add-tocart
# class AddCartView(APIView):
#     serializer_class=CartSerializer
#     queryset=Carts.objects.all()
#     authentication_classes=[authentication.TokenAuthentication]
#     permission_classes=[permissions.IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         id=kwargs.get("pk")
#         cake_obj=Cakes.objects.get(id=id)
#         serializer=CartSerializer(data=request.data)
#         if serializer.is_valid():
#             qs=Carts.objects.create(cake=cake_obj,user=request.user,qty=serializer.validated_data.get("qty"))
#             serializer=CartSerializer(qs)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)


class CartlistView(GenericViewSet,ListModelMixin):
    serializer_class=CartSerializer
    queryset=Carts.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)
    
class ReviewlistView(GenericViewSet,ListModelMixin):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Reviews.objects.filter(user=self.request.user)
    