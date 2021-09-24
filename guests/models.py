from django.db import models


class Party(models.Model):
    name = models.TextField()
    creation_dt = models.DateTimeField('creation datetime')

    def __str__(self) -> str:
        return self.name


class Guest(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    meal = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.full_name
