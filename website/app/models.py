from django.db import models

# Create your models here.
class Driver(models.Model):
    bus_num = models.CharField(max_length=50, primary_key=True)
    bus_name = models.CharField(max_length=50)
    driver_id = models.IntegerField(unique=True)
    driver_username = models.CharField(max_length=50)
    driver_email = models.EmailField(max_length=254)
    driver_password = models.CharField(max_length=254)
    driver_name = models.CharField(max_length=50)
    bus_route = models.CharField(max_length=255)
    latest_stop_name = models.CharField(max_length=50, blank=True, null=True)
    fare = models.CharField(max_length=255)
    emission_compliance = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(max_length=50)
    current_latitude = models.CharField(max_length=50, blank=True, null=True)
    current_longitude = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.driver_name


class Passenger(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    current_bus_id = models.CharField(max_length=50, blank=True, null=True)
    current_fare = models.IntegerField(blank=True, null=True)
    current_latitude = models.CharField(max_length=50, blank=True, null=True)
    current_longitude = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
