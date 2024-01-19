from django.urls import path
from . import views



urlpatterns = [
    path('', views.TeamAPIView.as_view(), name="Teams"), #url for teams api(create , get details , update team , remove team)
    path('<str:uuid>', views.team_details.as_view(), name="Teams"),
]