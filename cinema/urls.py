from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    genre_list,
    genre_detail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet,
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallDetail.as_view(), name="cinema-hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
