from django.test import TestCase
from django.core.urlresolvers import resolve
from unittest import skip


from app4apps.views import app_page
from app4apps.services import text_gen


class App4AppsTest(TestCase):
	def test_app4app_url_resolves_to_app4app_view(self):
		found = resolve('/app4apps/')
		self.assertEqual(found.func, app_page)


class TextGenServiceTest(TestCase):


	def test_returns_text(self):
		text = text_gen.new()
		assertEqual(text, "Random Text")
	
	@skip
	def test_returns_different_text(self):
		pass
	
	@skip
	def test_returns_text_associated_to_category(self):
		pass

