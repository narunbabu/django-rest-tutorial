from rest_framework import serializers
from gnippets.models import Dinosaur, LANGUAGE_CHOICES, STYLE_CHOICES

class GnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ('id','teeth', 'species',)

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

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
        instance.teeth = validated_data.get('teeth', instance.teeth)
        instance.species = validated_data.get('species', instance.species)
        instance.save()
        return instance
