# DFB38_04_mesg_board/mb_posts_app/tests.py

from django.test import TestCase
from django.urls import reverse

from .models import MbPost

class MbPostModelTest(TestCase):
	""" Test MbPost """

	_T1_obj_1 = "This is mb-post text"


	def setUp(self):
		""" """
		MbPost.objects.create(mbPostText=self._T1_obj_1)

	def test_01(self):
		""" test attrib MbPost.mbPostText """

		mbPost = MbPost.objects.get(id=1)
		print(f"@@@@ mbPost id=1 is {mbPost}")

		gotStg = f"{mbPost.mbPostText}"
		expStg = self._T1_obj_1
		self.assertEqual(gotStg, expStg)


class HomePageViewTest(TestCase):
	""" Test home page view HomePageView """

	_T1_obj_1 = "This is mb-post text _T1_obj_1"


	def setUp(self):
		""" """
		MbPost.objects.create(mbPostText=self._T1_obj_1)

	def test_01(self):
		""" Test getting a home page """
		resp = self.client.get("/")
		self.assertEqual(resp.status_code, 200)

	def test_02(self):
		""" Test getting home by reverse lookup
		This is supposed to test 'does it use HomePageView
		as the view', but it does not appear to do that
		directly(?!)
		"""
		h = reverse("home")
		self.assertEqual(h, "/")
		# (this repeats what test_01 does)
		resp = self.client.get(reverse("home"))
		self.assertEqual(resp.status_code, 200)

	def test_03(self):
		""" Is 'home.html' used as the template? """
		resp = self.client.get(reverse("home"))
		# django.template.response.TemplateResponse 
		#  <TemplateResponse status_code=200, "text/html; charset=utf-8>
		#print(f"@@@ resp is {type(resp)} {resp}")
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, "home.html")

### end ###
