from dinosaurs.models import Dinosaur
from rest_framework import serializers


class DinosaurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ('url', 'species','id')


class DinosaurSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ('url', 'species','teeth','id')
