from rest_framework import viewsets
from app.serializers import CustomerSerializer
from app.models import Customer
from rest_framework import generics


class CustomerListViewSet(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
