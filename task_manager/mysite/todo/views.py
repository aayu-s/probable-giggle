from todo.serializers import UserInfoSerializer, ListDetailSerializer, ListSerializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .models import List


class ListView(APIView):
    def get(self, request, format=None):
        user = request.user
        if user.id is not None:
            serializer = UserInfoSerializer(user)
            return Response(data=serializer.data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)


class ListItemView(APIView):
    def get(self, request, list_id, format=None):
        try:
            list = List.objects.filter(Q(owner=request.user.id) | Q(
                shared_with__in=(request.user.id, ))).distinct().get(pk=list_id)
            serializer = ListDetailSerializer(list)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={"error": "No list found"}, status=HTTP_400_BAD_REQUEST)

class CreateList(APIView):
    def post(self, request, format=None):
        data = request.data
        user = request.user
        data['owner'] = user.id
        try:
            serializer = ListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error": "List not saved"}, status=HTTP_400_BAD_REQUEST)

class DeleteList(APIView):
    def post(self, request, list_id, format=None):
        try:
            list = List.objects.get(pk=list_id)
            list.is_deleted=True
            list.save()
            return Response(data={"success":"Deletion done"}, status=HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error": "Could not delete list"}, status=HTTP_400_BAD_REQUEST)