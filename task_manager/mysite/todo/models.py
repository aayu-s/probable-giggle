from django.db import models
from django.contrib.auth.models import User


class TimestampModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class List(TimestampModel):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    sort_order = models.PositiveIntegerField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name='%(class)ss', on_delete=models.SET_NULL, null=True)
    shared_with = models.ManyToManyField(User, related_name='shared_%(class)ss', blank=True, null=True)

    class Meta:
        verbose_name = "List"
        
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    is_endstatus = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Statuse"
    
    def __str__(self) -> str:
        return self.name


class Item(TimestampModel):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    list = models.ForeignKey(List, related_name='%(class)ss', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, related_name='%(class)ss', on_delete=models.SET_NULL, null=True)
    assignee = models.ForeignKey(User, related_name='%(class)ss', on_delete=models.SET_NULL, null=True)
    sort_order = models.PositiveIntegerField()

    class Meta:
        verbose_name = "List Item"
