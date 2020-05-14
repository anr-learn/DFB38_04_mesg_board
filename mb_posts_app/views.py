# DFB38_04_mesg_board/mb_posts_app/views.py

#from django.shortcuts import render

from django.views.generic import ListView

from .models import MbPost

class HomePageView(ListView):
	model = MbPost
	template_name = "home.html"
	context_object_name = "all_mbposts_list"


### end ###
