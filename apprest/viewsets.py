from rest_framework import generics, viewsets
from .serializers import PersonSerializer
from app.models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
