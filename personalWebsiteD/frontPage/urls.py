from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("collin", views.collin, name = "collin"),
    path("<str:name>", views.greet, name="greet")
]