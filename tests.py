from django.test import TestCase
from django.core.urlresolvers import resolve
from unittest import skip


from app4apps.views import app_page
from app4apps.services import new_text


class App4AppsTest(TestCase):
	def test_app4app_url_resolves_to_app4app_view(self):
		found = resolve('/app4apps/')
		self.assertEqual(found.func, app_page)


class TextGenServiceTest(TestCase):
	def test_returns_backup_text(self):
		text = new_text("dog")
		self.assertEqual(text, "This category is not supported.")
	
	def test_returns_different_text(self):
		text1 = new_text("business")
		text2 = new_text("education")
		self.assertNotEqual(text1, text2)
	

