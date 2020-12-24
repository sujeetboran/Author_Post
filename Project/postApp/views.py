from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from django.core import serializers
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import requests
#for pagination
#from django.core.paginator import Paginator, EmptyPage

#costom responce class for givin response

class CustomResponse():
    def successResponse(self, data, status=status.HTTP_200_OK, description="SUCCESS"):
        return Response(
            {
                "success": True,
                "errorCode": 0,
                "description": description,
                "info": data
            }, status=status)

    def errorResponse(self, data={}, description="ERROR", errorCode=1, status=status.HTTP_200_OK):
        return Response(
            {
                "success": False,
                "errorCode": errorCode,
                "description": description,
                "info": data
            }, status=status)


@api_view(['POST'])
def register(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse().successResponse(request.data, description="User is created")
        else:
            return CustomResponse().errorResponse(description=serializer.errors)


@api_view(['POST'])
def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.data["username"])
        except Exception as error:
            return CustomResponse().errorResponse(description="invalid username")
        if user.password ==request.data["password"]:
            return CustomResponse().errorResponse(description="user login successfully")
        else:
            return CustomResponse().errorResponse(description="wrong password")


class posts(APIView):
    permission_classes = [AllowAny]

    #pagination_class = CustomPagination
    def get(self, request, format=None):

        #field for filtring
        title = request.data.get("title")
        author = request.data.get("author")
        sorting = request.data.get("sort")
        order = request.data.get("order")

        if title is not None and author is not None:
            posts = post.objects.filter(title=title).filter(author=author)

        elif sorting is not None and order is not None:
            if order == "asc":
                posts = post.objects.all().order_by(sorting)
            else:
                posts = post.objects.all().order_by(sorting)[::-1]

        # elif:
        else:
            posts = post.objects.all()

        #pagination code
        #field_names = [field.name for field in post._meta.get_fields()]
        #paginator = Paginator(queryset, 10)
        #print(offset)
        #if int(offset)>paginator.num_pages :
        #    return CustomResponse().errorResponse({},description="The page you are looking for doesnot exist")
        #results = paginator.page(offset)
        #output = []
        #for result in results:
        #    dic = {}
        #    for i in range(len(field_names)):
        #        dic[field_names[i]] = result[i]
        #        # pass
        #    output.append(dic)



        serializers = postSerializer(posts, many=True)
        try:
            return CustomResponse().successResponse(serializers.data, description="Fetched the details")
        except Exception as error:
            return CustomResponse().errorResponse(description=str(error))

    def post(self, request, format=None):

        data = request.data
        print(data)
        print(data["posts"])
        print(data["authors"])

        for authorObject in data["authors"]:
            print(authorObject)
            serializer = authorSerializer(data=authorObject)
            if serializer.is_valid():
                serializer.save()
            else:
                return CustomResponse().errorResponse(description=serializer.errors)
        for postObject in data["posts"]:
            print(postObject)
            serializer = postSerializer(data=postObject)
            if serializer.is_valid():
                serializer.save()
            else:
                return CustomResponse().errorResponse(description=serializer.errors)
        return CustomResponse().successResponse(data, description="data is added")


class postsDetails(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):

        try:
            postObject = post.objects.get(ID=pk)
            serializer = postSerializer(postObject)
            return CustomResponse().successResponse(serializer.data, description="post data")
        except Exception as error:
            return CustomResponse().errorResponse(description=str(error))

    def patch(self, request, pk):
        try:
            postObject = post.objects.get(ID=pk)
            serializer = postSerializer(postObject, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse().successResponse(serializer.data, description="post data patched")
            return CustomResponse().errorResponse(description=serializer.errors)
        except Exception as error:
            return CustomResponse().errorResponse(description=str(error))

    def delete(self, request, pk, format=None):

        try:
            postObject = post.objects.get(ID=pk)
            postObject.delete()
            return CustomResponse().successResponse({}, description="post deleted")
        except Exception as error:
            return CustomResponse().errorResponse(description=str(error))


class authorDetails(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk, format=None):
        try:
            authorObject = authors.objects.get(ID=pk)
        except Exception as error:
            return CustomResponse().errorResponse(description=str(error))
        data = request.data
        serializer = authorSerializer(authorObject, data=data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse().successResponse(serializer.data, description="author details updated")
        return CustomResponse().errorResponse(description=serializer.errors)
