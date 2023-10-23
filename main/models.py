from django.db import models
from common.models import User

class Notification(models.Model):
    Index = models.AutoField(primary_key=True)
    # ID = models.CharField(max_length=30)
    ID = models.ForeignKey(User, related_name='notify_ids', db_column='ID', on_delete=models.CASCADE)
    reason = models.IntegerField()
    # userID = models.CharField(max_length=30)
    userID = models.ForeignKey(User, related_name='notify_userIDs', db_column='userID', on_delete=models.CASCADE)
    date = models.CharField(max_length=20)

    class Meta:
        db_table='notify'
        managed=False