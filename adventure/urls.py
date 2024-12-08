from django.urls import path
from . import views

urlpatterns = [
    path("start/", views.start_game),
    path("state/<str:player_id>", views.get_state),
    path("choose/", views.choose)
]