from util import *

# Add your import statements here
from nltk.stem import WordNetLemmatizer



class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = None
		reducedText = []
		#Fill in code here

		lemmatizer = WordNetLemmatizer()
		for s in text:
                        temp = []
                        for w in range(len(s)):
                                temp.append(lemmatizer.lemmatize(s[w]))
                        reducedText.append(temp)
		
		return reducedText


