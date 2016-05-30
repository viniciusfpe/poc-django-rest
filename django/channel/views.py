import logging

from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from channel.models import Channel
from channel.serializers import ChannelSerializer
from django.conf import settings

class ChannelList(APIView):
    """
    List all channels, or create a new channel.
    """

    def get(self, request, format=None):

        channel = Channel.objects.all()
        serializer = ChannelSerializer(channel, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        """
        ---
        response_serializer: ChannelSerializer
        parameters:
            - name: body
              pytype: ChannelSerializer
              paramType: body
        """
        serializer = ChannelSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChannelDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ChannelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)