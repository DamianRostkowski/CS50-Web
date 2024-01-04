from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("bomba", views.bomba, name="bomba"),
    path("<str:name>", views.greet, name="greet"),
    path("greet/<str:name>", views.greet, name="greet"),
]
