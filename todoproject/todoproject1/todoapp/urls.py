from django.urls import path,include
from todoapp import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailview.as_view(), name="cbvdetails"),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')

    ]
