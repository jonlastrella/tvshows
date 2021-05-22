from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/<int:showId>', views.singleShow),
    path('shows/<int:showId>/edit', views.editShow),
    path('shows/new', views.newShow),
    path('shows/create', views.create),
    path('shows/<int:showId>/update', views.updateShow),
    path('shows/<int:showId>/delete', views.deleteShow)
]
