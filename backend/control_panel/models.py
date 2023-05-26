from django.db import models


class Master(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title


class Salon(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    def get_timeslot_repr(self):
        for slot in self.TIME_SLOTS:
            if slot[0] == self.time_slot:
                yield slot[1]

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
    date = models.DateField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        timeslot_rept = next(self.get_timeslot_repr())
        return (
            f'{timeslot_rept} | {self.date} | {self.master} |'
            f' {self.procedure} | {self.salon} | {self.client}'
        )