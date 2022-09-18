from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('boards/<int:pk>/',views.board_topics,name='board_topics'),
    path('new_topic/<int:pk>/',views.new_topic,name='new_topic')
]