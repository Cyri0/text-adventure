from . import models
from rest_framework.serializers import ModelSerializer, IntegerField, CharField, Serializer

class ChoiceSerializer(Serializer):
    id = IntegerField()
    text = CharField()

class LocationSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = models.Location
        fields = ['name', 'description', 'choices']

class PlayerCreatorSerializer(ModelSerializer):
    class Meta:
        model = models.PlayerStatus
        fields = '__all__'
        depth = 1