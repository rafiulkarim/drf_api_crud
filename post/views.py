from msilib.schema import Class
from django.shortcuts import render
from . models import *
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .serializers import CommentSerializer


# Create your views here.
class PostList(APIView):
    def get(self, request, format=None):
        intance = Post.objects.all()
        serializer = PostSerializer(intance, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 200}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        intance = self.get_object(pk)
        serializer = PostSerializer(intance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = PostSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 200})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'success': 200}, status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    def get(self, request, format=None):
        intance = Comment.objects.all()
        serializer = CommentSerializer(intance, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 200}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommenttDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    
    def get(self, request, pk, format=None):
        intance = self.get_object(pk)
        serializer = CommentSerializer(intance)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = CommentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 200})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'success': 200}, status=status.HTTP_204_NO_CONTENT)





    
