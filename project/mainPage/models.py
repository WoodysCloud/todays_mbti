from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    writer = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ", " + self.title + ", " + self.content + ", " + self.writer + ", " + self.comment

class Reply(models.Model):
    bid = models.IntegerField()
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ", " + self.bid + ", " + self.content + ", " + self.writer

class Interior_obj(models.Model):
    category = models.CharField(max_length=20)
    obj_name = models.CharField(max_length=50)
    detail_link = models.CharField(max_length=200)
    minimal = models.IntegerField()
    modern = models.IntegerField()
    vintage = models.IntegerField()
    natural = models.IntegerField()
    individuality = models.IntegerField()
    romantic = models.IntegerField()
    casual = models.IntegerField()
    useful = models.IntegerField()
    enfj = models.FloatField()
    enfp = models.FloatField()
    entj = models.FloatField()
    entp = models.FloatField()
    esfj = models.FloatField()
    esfp = models.FloatField()
    estj = models.FloatField()
    estp = models.FloatField()
    infj = models.FloatField()
    infp = models.FloatField()
    intj = models.FloatField()
    intp = models.FloatField()
    isfj = models.FloatField()
    isfp = models.FloatField()
    istj = models.FloatField()
    istp = models.FloatField()
    like = models.IntegerField()
    photo_link = models.CharField(max_length=200)




