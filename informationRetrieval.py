from util import *
import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cs
# Add your import statements here




class InformationRetrieval():

    def __init__(self):
        self.index = None

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
                A list of lists of lists where each sub-list is
                a document and each sub-sub-list is a sentence of the document
        arg2 : list
                A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """

        index = None

        #Fill in code here
        restored_docs=[]
        for d in docs:
            temp=''
            for i in range(len(d)):
                s=d[i]
                for j in range(len(s)):
                    w=s[j]
                    if i==len(d)-1 and j==len(s)-1: temp+=w
                    else: temp+=w+' '
            restored_docs.append(temp)
        
        
        vectorizer=TfidfVectorizer(use_idf=True)
        X=vectorizer.fit_transform(restored_docs)
        df=pd.DataFrame(X[:].todense(), columns=vectorizer.get_feature_names())
        unique_words=vectorizer.get_feature_names()
        
        self.rest_docs=restored_docs
        self.df=df


        self.index = index


    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
                A list of lists of lists where each sub-list is a query and
                each sub-sub-list is a sentence of the query
        arg2: list
                A list of lists of lists where each sub-list is a query and
                each sub-sub-list is a sentence of the doc

        Returns
        -------
        list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        """

        doc_IDs_ordered = []

        #Fill in code here
        restored_queries=[]
        for q in queries:
            temp=''
            for i in range(len(q)):
                s=q[i]
                for j in range(len(s)):
                    w=s[j]
                    if i==len(q)-1 and j==len(s)-1: temp+=w
                    else: temp+=w+' '
            restored_queries.append(temp)

        '''restored_docs=[]
        for d in docs:
            temp=''
            for i in range(len(d)):
                s=d[i]
                for j in range(len(s)):
                    w=s[j]
                    if i==len(d)-1 and j==len(s)-1: temp+=w
                    else: temp+=w+' '
            restored_docs.append(temp)
'''
        vectorizer=TfidfVectorizer(use_idf=True)
        X=vectorizer.fit_transform(self.rest_docs)
 #       df=pd.DataFrame(X[:].todense(), columns=vectorizer.get_feature_names())
 #       unique_words=vectorizer.get_feature_names()
        
        
        q_tfidf=pd.DataFrame(vectorizer.transform(restored_queries).todense(), columns= vectorizer.get_feature_names())
        qd_sim=cs(np.array(q_tfidf),np.array(self.df))

        ranking=np.zeros((qd_sim.shape[0],qd_sim.shape[1]))
        for i in range(len(qd_sim)):
            ranking[i]=(-qd_sim[i,:]).argsort()+1
        
        doc_IDs_ordered=ranking
        return doc_IDs_ordered
