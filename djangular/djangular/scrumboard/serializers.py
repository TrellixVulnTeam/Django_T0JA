from rest_framework import serializers
from .models import List, Card

# rest framework is used to send data from backend to front end in JSON
# serializers converts these data into JSON
# ModelSerializer will look up your module, will look up their fields and convert them to JSON

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'