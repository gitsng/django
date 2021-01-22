from django.urls import path

from . import views

urlpatterns = [
    path('',views.todo_list,name='todo-list'),
    path('add',views.todo_add),
    path('remove/<int:task_id>',views.remove_todo),
]