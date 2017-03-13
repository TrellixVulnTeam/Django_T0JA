from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer, CardSerializer
from rest_framework import permissions
from .models import List, Card

# These are view classes. They are basically the components that goes through the request by the user and will retrive the data it need JSON. and will send it back

class ListViewSets(ModelViewSet):
    queryset = List.objects.all()                           # List is List models class. Object = query get all() will give back the list of python objects
    serializer_class = ListSerializer                       # point the listView to listSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CardViewSets(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)      #, added becoz its a tuple, and tuple with a single element always needs a
                                                              #  , otherwise it would be considered     as a single element

