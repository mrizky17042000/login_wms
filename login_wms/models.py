from django.db import models


class Role(models.Model):
    id_role = models.IntegerField(primary_key=True)
    name_role = models.CharField(max_length=25, blank=False, null=True)

    class Meta:
        db_table = 'role'


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=25, blank=False, null=True)
    password = models.CharField(max_length=25, blank=False, null=True)
    id_role = models.ForeignKey(
        Role, models.DO_NOTHING, db_column='id_role', blank=True, null=True)

    class Meta:
        db_table = 'user'
