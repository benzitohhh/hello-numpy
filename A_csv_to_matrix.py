import csv
from collections import defaultdict
from numpy import *
import scipy.io as sio

pat_fams = []

# for now, only use keywords / classifications / citations
all_keywords        = defaultdict(int)
all_classifications = defaultdict(int)
all_citations       = defaultdict(int)

with open('small.tsv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for (accession, titles, keywords, classifications, citations, assignees) in reader:
        titles, keywords, classifications, citations, assignees = \
            map(lambda x: x.split('|'), [titles, keywords, classifications, citations, assignees])
        
        pat_fams.append((accession, titles, keywords, classifications, citations, assignees))
        
        for kw in keywords:
            all_keywords[kw] += 1
        for cl in classifications:
            all_classifications[cl] += 1
        for ci in citations:
            all_citations[ci] += 1
        
rows = []
for (accession, titles, keywords, classifications, citations, assignees) in pat_fams:
    # keywords
    kws = set(keywords)
    k_row = map(lambda x: 1 if x in kws else 0, all_keywords.keys())
    
    # classifications
    cls = set(classifications)
    cl_row = map(lambda x: 1 if x in cls else 0, all_classifications.keys())
    
    # citations
    cis = set(citations)
    ci_row = map(lambda x: 1 if x in cis else 0, all_citations.keys())

    row = k_row + cl_row + ci_row
    rows.append(row)

X = matrix(rows)

# export X
# export pat_fams, all_keywords, all_classifications, all_citations

sio.savemat('please.mat', {'X':X, 'pat_fams':pat_fams, 'all_keywords':all_keywords, 'all_classifications':all_classifications, 'all_citations':all_citations})
        
