from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    old_password = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Customer(models.Model):
    #INTERESTS_CATEGORIES = ()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dni = models.CharField(primary_key=True, max_length=15)
    both_date = models.DateField()
    phone_number = models.CharField(max_length=10, blank=False)
    #interests = models.CharField(max_length=INTERESTS_CATEGORIES.count(), choices=INTERESTS_CATEGORIES)
