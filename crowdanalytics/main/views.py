from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from . import models


class AnnotatorViewSet(viewsets.ModelViewSet):
    queryset = models.Annotator.objects.all().order_by('abstract_user')
    serializer_class = serializers.AnnotatorSerializer