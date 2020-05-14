# DFB38_04_mesg_board/mb_posts_app/urls.py

from django.urls import path

from .views import HomePageView

urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
	]

### end ###
