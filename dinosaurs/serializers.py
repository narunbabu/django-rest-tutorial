# from dinosaurs.models import Dinosaur
from rest_framework import serializers
from dinosaurs.models import Dinosaur, LANGUAGE_CHOICES, STYLE_CHOICES

class DinosaurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ('id','teeth', 'species',)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Dinosaur.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.id = validated_data.get('id', instance.id)
        # instance.url = validated_data.get('url', instance.url)
        instance.teeth = validated_data.get('teeth', instance.teeth)
        instance.species = validated_data.get('species', instance.species)
        instance.save()
        return instance

# class DinosaurSerializer2(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Dinosaur
#         fields = ('url', 'species','teeth','id')
