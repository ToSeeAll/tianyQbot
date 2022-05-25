from django.db import models


class Config(models.Model):
    id = models.AutoField
    qq = models.CharField(max_length=20)
    sex = models.CharField(max_length=2)

    class Meta:
        db_table = 'user'
        app_label = 'tianyQbot'
