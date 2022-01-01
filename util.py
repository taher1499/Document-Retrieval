# Add your import statements here
# Add any utility functions here

def rel_docs(query_id,qrels):
    j=[item['id'] for item in qrels if item['query_num']==str(query_id)]
    return j

def rel_score_as_dict_for_query(query_id,qrels):
    docs_score_dict={int(item['id']):int(item['position']) for item in qrels if int(item['query_num'])==int(query_id)}
    return docs_score_dict
    
def rel_score_for_query(query_id,qrels):
    score=[int(item['position']) for item in qrels if int(item['query_num'])==int(query_id)]
    i_d=[int(item['id']) for item in qrels if int(item['query_num'])==int(query_id)]
    score_id=list(map(lambda x,y: [x,y],score,i_d))
    return score_id
