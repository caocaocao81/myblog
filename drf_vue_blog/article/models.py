# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artical(models.Model):
    artical_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    artical_title = models.TextField()
    artical_content = models.TextField()
    artical_views = models.BigIntegerField(blank=True, null=True,default=0)
    artical_comment_count = models.IntegerField(blank=True, null=True,default=0)
    create_time = models.DateTimeField(blank=True, null=True)
    artical_like_count = models.BigIntegerField(blank=True, null=True,default=0)

    class Meta:
        managed = False
        db_table = 'artical'


class ArticalLabel(models.Model):
    artical_id = models.AutoField(primary_key=True)
    label_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'artical_label'


class ArticalSort(models.Model):
    artical_id = models.IntegerField(primary_key=True)
    sort_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'artical_sort'
        unique_together = (('artical_id', 'sort_id'),)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    artical_id = models.IntegerField()
    comment_like_count = models.IntegerField(blank=True, null=True,default=0)
    comment_date = models.DateField(blank=True, null=True,default=0)
    comment_content = models.TextField()
    parent_comment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'


class Labels(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField(max_length=20)
    label_alias = models.CharField(max_length=15)
    label_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labels'


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    user_profile_photo = models.CharField(max_length=255)
    user_birthday = models.DateField(blank=True, null=True)
    user_telephone = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'user_info'
