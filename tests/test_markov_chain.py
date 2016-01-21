
from django.test import TestCase
from django.core.urlresolvers import resolve
from unittest import skip

from app4apps.services import new_text
from app4apps.training.markov import chain_maker 
from app4apps.training.markov import chain

import pickle

class MarkovChainTest(TestCase):
	''' I want to test that the Markov chain is running 
		that it is loaded properly when the site is running
		that it doesn't load itself over and over again
	
		main operations of the chain are:
			loading the dictionary
			returning 		
			
	'''

	def setUp(self):
		self.mc = chain.load_markov_chain("business")

	def tearDown(self):
		self.mc = None

	def test_loads_chain_class(self):
		self.assertIsInstance(self.mc, chain_maker.markov_state) 

	def test_loads_different_chain_for_each_category(self):
		mc_finance  = chain.load_markov_chain("finance")
		self.assertNotEqual(self.mc, mc_finance)

	def test_chain_returns_text(self):
		text = chain.text_from_chain(self.mc)		
		self.assertIsInstance(text, str)
	
	def test_chain_is_length_50_words(self):
		desired_length = 50
		text = chain.text_from_chain(self.mc, desired_length)
		self.assertEqual(len(text.split()), desired_length, 
			"Length of text is not 50, but instead %s"%len(text.split()))



class ChainMakerTest(TestCase):
	def setUp(self):
		self.mc = chain.load_markov_chain("business")
		self.d1 = {'a':1, 'b':2, 'c':3}
		self.d2 = {'b':2, 'c':1, 'd':4}
		self.d3 = {'a':1, 'b':4, 'c':3, 'd':4}

	def tearDown(self):
		self.d1 = None
		self.d2 = None
		self.d3 = None
		self.mc = None

	def test_merge(self):
		res = self.mc.merge(self.d1,self.d2)
		self.assertEqual(self.d3, res)	

	def test_getNextWord(self):
		word = self.mc.getNextWord(self.d3)
		self.assertIn(word, self.d3.keys())

















