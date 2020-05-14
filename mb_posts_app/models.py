# mb_posts_app/models.py

from django.db import models

# 'Post' in the DFB book
class MbPost(models.Model):

	# 'text' in the book
	mbPostText = models.TextField()



### end ###
