from django.db import models
from common.models import User, CustomUser

class Notification(models.Model):
    Index = models.AutoField(primary_key=True)
    ID = models.ForeignKey(User, related_name='notify_ids', db_column='ID', on_delete=models.CASCADE)
    reason = models.IntegerField()
    userID = models.ForeignKey(User, related_name='notify_userIDs', db_column='userID', on_delete=models.CASCADE)
    # date = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        db_table = 'notify'
        managed = False

# class NotifyRead(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     notify = models.ForeignKey(Notification, on_delete=models.CASCADE)
#     read_at = models.DateTimeField(auto_now_add=True)

class Notice(models.Model):
    index = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # register_day = models.CharField(max_length=20, blank=True, null=True)
    register_day = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'noticeboard'
        managed = False