# mb_posts_app/models.py

from django.db import models

# 'Post' in the DFB book
class MbPost(models.Model):

	# 'text' in the book
	mbPostText = models.TextField()

	def __str__(self):
		return ("%s: %s" % 
			(self.__class__.__name__, self.mbPostText[:50]))



### end ###
