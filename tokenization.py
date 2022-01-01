from util import *

# Add your import statements here
from nltk.tokenize import TreebankWordTokenizer



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None
		tokenizedText = []
		#Fill in code here
		for i in range(len(text)):
                        tokenizedText.append(text[i].split(' '))

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None
		tokenizedText = []
		#Fill in code here
		for s in range(len(text)):
                        tokenizedText.append(TreebankWordTokenizer().tokenize(text[s]))
		return tokenizedText
