from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer, CardSerializer
from .models import List, Card

# These are view classes. They are basically the components that goes through the request by the user and will retrive the data it need JSON. and will send it back

class ListViewSets(ModelViewSet):
    queryset = List.objects.all()                           # List is List models class. Object = query get all() will give back the list of python objects
    serializer_class = ListSerializer                       # point the listView to listSerializer

class CardViewSets(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

