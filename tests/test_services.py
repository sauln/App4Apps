from django.test import TestCase
from django.core.urlresolvers import resolve
from unittest import skip

from app4apps.services import new_text
from app4apps.training.markov import markov_chain




class MarkovChainTest(TestCase):
	''' I want to test that the Markov chain is running 
		that it is loaded properly when the site is running
		that it doesn't load itself over and over again
	
		main operations of the chain are:
			loading the dictionary
			returning 		
			
	'''
	
	def test_loads_chain(self):
		mc = markov_chain.load_markov_chain("business")
		self.assertIsInstance(mc,markov_chain) 


	def test_loads_different_chain_for_each_category(self):
		mc_business = markov_chain.load_markov_chain("business")
		mc_finance  = markov_chain.laod_markov_chain("finance")
		self.assertNotEqual(mc_business, mc_finance)








class TextGenServiceTest(TestCase):
	def test_returns_text(self):
		text = new_text("")
		self.assertNotEqual(text, "")


	@skip
	def test_returns_from_correct_category(self):
		print("I'm not sure how to test something that is not deterministic")

	def test_returns_no_category(self):
		text = new_text("dog")
		self.assertEqual(text, "This category is not supported.")
	
	def test_returns_different(self):
		text1 = new_text("business")
		text2 = new_text("education")
		self.assertNotEqual(text1, text2)
	

