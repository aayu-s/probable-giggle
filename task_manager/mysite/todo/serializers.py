from django.contrib.auth.models import User
from rest_framework.serializers import ListSerializer
from .models import Item, List
from django.db.models import Q
from rest_framework import serializers

class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ListDetailSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, read_only=True)
    class Meta:
        model = List
        fields = ('id', 'name', 'items')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'name', 'owner')

class UserInfoSerializer(serializers.ModelSerializer):
    lists = serializers.SerializerMethodField('get_non_deleted')
    def get_non_deleted(self,user):
        qs = List.objects.filter(is_deleted=False).filter(Q(owner=user)|Q(shared_with=user))
        lists = ListSerializer(instance=qs,many=True)
        return lists.data
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'lists', 'shared_lists')
