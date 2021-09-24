from django.urls import path

from . import views


app_name = 'guests'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:party_id>/", views.detail, name="detail"),
    path("<int:party_id>/modify/", views.modify, name="modify"),
]
