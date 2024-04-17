from django.db import models

# Create your models here.
class System_User(models.Model):
    
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Driver(System_User):
    driver_charges=models.IntegerField()


    def __str__(self):
        return self.driver_charges


class vehicles(models.Model):
    number_plate=models.CharField(max_length=255)
    max_weight=models.IntegerField()
    driver=models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.number_plate
    

class Trips(models.Model):
    start_position=models.IntegerField()
    end_point=models.IntegerField()
    status=models.BooleanField()
    vehicle=models.ForeignKey(vehicles, on_delete=models.CASCADE)
    def __str__(self):
        return self.status
    

class Payments(models.Model):
    trip=models.OneToOneField(Trips, on_delete=models.CASCADE, primary_key=True)
    amount=models.IntegerField()
    status=models.BooleanField()

    def __str__(self):
        return self.amount
    

class Clients(models.Model):
    joining_date=models.DateField()

    def __str__(self):
        return self.joining_date







