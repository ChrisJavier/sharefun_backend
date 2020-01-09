from rest_framework import serializers
from app.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['dni', 'last_name', 'first_name']
