from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=30, primary_key=True)
    userEmail = models.EmailField(max_length=45)
    userNickname = models.CharField(max_length=8)
    userAge = models.IntegerField()
    userSex = models.IntegerField()
    userWeight = models.IntegerField()
    userWD = models.CharField(max_length=10)
    anaerobicScore = models.FloatField(default=0.0)
    aerobicScore = models.FloatField(default=0.0)
    Score = models.FloatField(default=0.0)
    AgeRank = models.IntegerField(null=True, blank=True)
    CustomRank = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table='userTBL'
        managed=False