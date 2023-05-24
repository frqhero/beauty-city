from django.db import models


class Master(models.Model):
    name = models.CharField(max_length=50)


class Procedure(models.Model):
    title = models.CharField(max_length=50)


class Salon(models.Model):
    title = models.CharField(max_length=50)


class Client(models.Model):
    name = models.CharField(max_length=50)


class Appointment(models.Model):
    TIME_SLOTS = [
        ('0', '10-11'),
        ('1', '11-12'),
        ('2', '12-13'),
        ('3', '13-14'),
        ('4', '14-15'),
        ('5', '15-16'),
        ('6', '16-17'),
        ('7', '17-18'),
        ('8', '18-19'),
        ('9', '19-20'),
    ]
    time_slot = models.CharField(max_length=1, choices=TIME_SLOTS)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
