from django.test import TestCase
from django.core.urlresolvers import resolve
from unittest import skip

from app4apps.services import new_text
from app4apps.training.markov import chain_maker 
from app4apps.training.markov import chain

import pickle



class TextGenServiceTest(TestCase):
	def test_returns_text(self):
		text = new_text("")
		self.assertNotEqual(text, "")


	@skip
	def test_returns_from_correct_category(self):
		print("I'm not sure how to test something that is not deterministic")

	def test_returns_no_category(self):
		text = new_text("dog")
		self.assertEqual(text, "This category is not supported")
	
	def test_returns_different(self):
		text1 = new_text("business")
		text2 = new_text("education")
		self.assertNotEqual(text1, text2)
	

