from django.test import TestCase
from django.core.urlresolvers import resolve

from app4apps.views import app_page

class App4AppsTest(TestCase):
	def test_app4app_url_resolves_to_app4app_view(self):
		found = resolve('/app4apps/')
		self.assertEqual(found.func, app_page)



