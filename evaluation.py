from util import *

# Add your import statements here
import numpy as np



class Evaluation():

    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The precision value as a number between 0 and 1
        """

        precision = -1

        #Fill in code here
        k_returned_docs=query_doc_IDs_ordered[:k]
        true_doc_IDs=[int(i) for i in true_doc_IDs]
        k_returned_docs=[int(i) for i in k_returned_docs]
        true_doc_IDs_set=set(true_doc_IDs)
        k_returned_docs_set=set(k_returned_docs)
        intersection=true_doc_IDs_set.intersection(k_returned_docs_set)
        precision=len(intersection)/k

        return precision


    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean precision value as a number between 0 and 1
        """

        meanPrecision = -1

        #Fill in code here
        totalPrecision=0
        for q in range(len(query_ids)):
            totalPrecision+=self.queryPrecision(doc_IDs_ordered[q],query_ids[q],rel_docs(query_ids[q],qrels),k)
        meanPrecision=totalPrecision/len(query_ids)
        return meanPrecision


    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The recall value as a number between 0 and 1
        """

        recall = -1

        #Fill in code here
        k_returned_docs=query_doc_IDs_ordered[:k]
        true_doc_IDs=[int(i) for i in true_doc_IDs]
        k_returned_docs=[int(i) for i in k_returned_docs]
        true_doc_IDs_set=set(true_doc_IDs)
        k_returned_docs_set=set(k_returned_docs)
        intersection=true_doc_IDs_set.intersection(k_returned_docs_set)
        recall=len(intersection)/len(true_doc_IDs_set)
        return recall


    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean recall value as a number between 0 and 1
        """

        meanRecall = -1

        #Fill in code here
        totalRecall=0
        for q in range(len(query_ids)):
            totalRecall+=self.queryRecall(doc_IDs_ordered[q],query_ids[q],rel_docs(query_ids[q],qrels),k)
        meanRecall=totalRecall/len(query_ids)
        return meanRecall


    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The fscore value as a number between 0 and 1
        """

        fscore = -1

        #Fill in code here
        precision=self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        recall=self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        if precision == 0  and recall == 0: fscore = 0
        else: fscore=(2*precision*recall)/(precision+recall)
        return fscore


    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean fscore value as a number between 0 and 1
        """

        meanFscore = -1

        #Fill in code here
        totalFscore=0
        for q in range(len(query_ids)):
            totalFscore+=self.queryFscore(doc_IDs_ordered[q],query_ids[q],rel_docs(query_ids[q],qrels),k)
        meanFscore=totalFscore/len(query_ids)
        return meanFscore

    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The nDCG value as a number between 0 and 1
        """

        nDCG = -1

        #Fill in code here
        return nDCG


    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean nDCG value as a number between 0 and 1
        """

        meanNDCG = -1

        #Fill in code here
        NDCG=0
        for q in range(len(query_ids)):
             
            score_id=rel_score_for_query(query_ids[q],qrels)
            score_id.sort()
             
            doc_id_ordered=doc_IDs_ordered[q]
            k_returned_docs=doc_id_ordered[:k]
            k_returned_docs=[int(i) for i in k_returned_docs]
        
        
            
            IDCG=0
            if len(score_id)<k:
                for i in range(len(score_id)):
                    IDCG+=(1/((score_id[i][0])*np.log2(2+i+1)))
            else:
                top_k_score_id=score_id[:k]
                for i in range(k):
                    IDCG+=(1/((top_k_score_id[i][0])*np.log2(2+i+1)))
            
            
           
            docs_score_dict=rel_score_as_dict_for_query(query_ids[q],qrels)
            DCG=0
            for i in range(len(k_returned_docs)):
                if k_returned_docs[i] in docs_score_dict.keys():
                    DCG+=(1/((int(docs_score_dict[k_returned_docs[i]]))*np.log2(2+i+1)))
                else: DCG+=0


            NDCG+=(DCG/IDCG)



        meanNDCG=NDCG/len(query_ids)
        return meanNDCG

    def queryAveragePrecision(self,query_doc_IDs_ordered,query_id,true_doc_IDs,k):
        """
        Computation of average precision of the Information Retrieval System
        at a given value of k for a single query (the average of precision@i
        values for i such that the ith document is truly relevant)

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The average precision value as a number between 0 and 1
        """

        avgPrecision = -1

        #Fill in code here
        docid_precision={}
        AP=0
        count=0
        k_returned_docs=query_doc_IDs_ordered[:k]
        true_doc_IDs=[int(i) for i in true_doc_IDs]
        k_returned_docs=[int(i) for i in k_returned_docs]
        for i in range(1,k+1):
            docid_precision[k_returned_docs[i-1]]=self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, i)
        for id in docid_precision.keys():
            if id in true_doc_IDs:
                AP+=docid_precision[id]
                count+=1
        if count==0: avgPrecision=0
        else: avgPrecision=AP/count
        return avgPrecision


    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
        """
        Computation of MAP of the Information Retrieval System
        at given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The MAP value as a number between 0 and 1
        """

        meanAveragePrecision = -1

        #Fill in code here
        totalAveragePrecision=0
        for q in range(len(query_ids)):
            totalAveragePrecision+=self.queryAveragePrecision(doc_IDs_ordered[q],query_ids[q],rel_docs(query_ids[q],q_rels),k)
        meanAveragePrecision=totalAveragePrecision/len(query_ids)
        return meanAveragePrecision
