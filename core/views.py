from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse

# Create your views here.


class AllUsersView(APIView):
    def get(self, request):

        users = models.User.objects.all()
        data = serializers.UserSerializer(users, many=True).data

        return JsonResponse(data, safe=False)


class UserView(APIView):
    def get(self, request, user_id):

        user = models.User.objects.filter(id=user_id).first()
        data = serializers.UserSerializer(user).data
        return JsonResponse(data)