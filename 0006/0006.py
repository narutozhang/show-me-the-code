

# 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# tf-idf

from a0004 import words_count
from sklearn import datasets
import numpy as np

news = datasets.fetch_20newsgroups()
texts = news.data[:100]

wc_total = words_count(texts)
wc_files = [words_count([x]) for x in texts]

# dictionary
dictionary = sorted(wc_total.keys())

# number of samples and words
n_samples = len(wc_files)
n_keys = len(dictionary)

# cal tf-idf matrix
matrix = np.zeros((n_samples, n_keys))
for i, wc_file in enumerate(wc_files):
    for word, count in wc_file.items():
        matrix[i, dictionary.index(word)] = count

# term frequence
tf = matrix / matrix.sum(axis=1, keepdims=True)
# inverse document frequence
idf = np.log10(n_samples / (matrix>0).sum(axis=0))

tf_idf = tf * idf

# result, top 10 tf-idf
keywords = []
for f in tf_idf:
    keywords.append([dictionary[index] for weight, index in sorted(zip(f, range(n_keys)), reverse=True)[:10]])
#   keywords.append(sorted(dictionary, key=lambda x:f[dictionary.index(x)], reverse=True)[:5])

# print(keywords[:5])
for k in keywords[:10]:
    print(','.join(k))
