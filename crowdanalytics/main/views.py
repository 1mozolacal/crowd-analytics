from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models


class AnnotatorViewSet(viewsets.ModelViewSet):
    queryset = models.Annotator.objects.all().order_by('abstract_user')
    serializer_class = serializers.AnnotatorSerializer

class TestAuthViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'You are': self.request.user.username}
        return Response(content)


class TestIsAuthViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'You are authenticated'}
        return Response(content)