from django.urls import path
from .views import ComentView,ComentSingleView
urlpatterns=[
    path('',ComentView.as_view()),
    path('<int:pk>/',ComentSingleView.as_view())
    ]