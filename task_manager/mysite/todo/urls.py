from django.urls import path

from .views import ListView, ListItemView, CreateList, DeleteList

urlpatterns = [
    path('get_my_lists', ListView.as_view()),
    path('get_list_items/<int:list_id>/', ListItemView.as_view()),
    path('create_list', CreateList.as_view()),
    path('delete_list/<int:list_id>/', DeleteList.as_view())
]
