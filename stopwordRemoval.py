from util import *

# Add your import statements here
from nltk.corpus import stopwords



class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = None
		stopwordRemovedText = []
		#Fill in code here
		remove_words = stopwords.words('english')
		for s in text:
                        temp =[]
                        for w in s:
                                if w not in remove_words:
                                        temp.append(w)
                        stopwordRemovedText.append(temp)

		
		return stopwordRemovedText




	
