from django.db import models


class User(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Cosmetics(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    ingredients = models.CharField(max_length=200)
