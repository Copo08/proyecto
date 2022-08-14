from django.urls import path
from persona import views


urlpatterns=[
    path('',views.PersonaView.as_view()),
    path('<int:id>',views.PersonaSingleView.as_view()),

]