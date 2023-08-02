from django.urls import path
from discussions import views

urlpatterns = [
   path('comment/create/<int:pk>/', views.create_comment, name='create_comment'),
   #path('resource/', views.resource_detail, name='resource_detail'),
   path('create/discussion', views.create_discussion, name='create_discussion'),
   path('display/discussion/<int:pk>/', views.discussion_detail, name='discussion_detail'),
   path('list/', views.discussion_list, name='discussion_list'),

]