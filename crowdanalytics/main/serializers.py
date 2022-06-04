from . import models
from rest_framework import serializers

class AbstractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AbstractUser
        fields = ['city','province','zip_code']

class AnnotatorSerializer(serializers.ModelSerializer):
    abstract_user = AbstractUserSerializer()

    class Meta:
        model = models.Annotator
        fields = ["abstract_user"]

