"""
Avery Lee
CSE 163 AB
This program implements the SearchEngine class for HW Search.
HW Search inputs a string query and returns a list of documents that
is the best search for that query in descending order.
Documents with higher TF-IDF scores are considered to be better searches.
"""


from document import Document
import os
import math
import re
import operator


class SearchEngine:
    """
    The SearchEngine class receives a corpus and
    returns a list of best searches by calculating the
    TF-IDF of each document in the corpus.
    """
    def __init__(self, directory):
        """
        Parameter: directory of corpus
        Initializes the directory, dictionary of documents,
        list of all unique words in corpus, and dictionary for inverted index
        """
        self._directory = directory
        # ex: {doc1: ['i', 'love', 'cats'], doc2: ['i', 'love', 'dogs']}
        # self._dict_of_docs = self._dict_of_documents()
        # list of all unique words in corpus
        self._all_unique = self._all_unique_list()
        # {term: list of docs}
        self._inverted_index = self._get_inverted_index()

    # my own
    # def _dict_of_documents(self):
    #     """
    #     Parameter: self
    #     Returns a dictionary of doc objects (key)
    #     and its unique words (value)
    #     If corpus empty, return {}
    #     """
    #     dict_docs = {}
    #     for filename in os.listdir(self._directory):
    #         doc = Document(os.path.join(self._directory, filename))
    #         dict_docs[doc] = doc.get_words()
    #     return dict_docs

    # my own
    def _all_unique_list(self):
        """
        Parameter: self
        Returns a list of all the unique words in the corpus
        If no words, return []
        """
        all_unique_words = []
        for filename in os.listdir(self._directory):
            doc = Document(os.path.join(self._directory, filename))
            for list_of_unique in doc.get_words():
                all_unique_words += list_of_unique
        return list(set(all_unique_words))
        # all_unique_words = []
        # for list_of_unique in self._dict_of_docs.values():
        #     all_unique_words += list_of_unique
        # return list(set(all_unique_words))

    # my own
    def _get_inverted_index(self):
        """
        Parameter: self
        Returns a dictionary of each word (key) and
        the doc objects that contain that term (value)
        If no term, return {}
        """
        # inverted = {}  # {word: [doc objects]}
        # for word in self._all_unique:
        #     docs_with_word = []  # ex: [doc1 object, doc3 object]
        #     for
        # inverted = {}  # {word: [doc objects]}
        # for word in self._all_unique:
        #     docs_with_word = []  # ex: [doc1 object, doc3 object]
        #     for k, v in self._dict_of_docs.items():
        #         if word in v:
        #             docs_with_word.append(k)
        #     inverted[word] = docs_with_word
        # return inverted

    # my own
    def _calculate_indiv_tfidf(self, term, doc):
        """
        Parameter: self, term (str), doc (object)
        Returns the TF-IDF (float) of a given term in a given doc
        """
        tfidf_indiv = doc.term_frequency(term) * self._calculate_idf(term)
        return tfidf_indiv

    # required
    def _calculate_idf(self, term):
        """
        Parameter: self, term (str)
        Returns the idf of the term in the corpus
        If term not in any docs, return 0
        """
        if term not in self._inverted_index.keys():
            return 0
        else:
            idf = math.log(float(len(self._dict_of_docs)) /
                           len(self._inverted_index[term]))

        return idf

    # required
    def search(self, query):
        """
        Parameter: query (str)
        Returns a list of tuples (doc object, tfidf) ordered
        by tfidf from greatest to least
        If none of the words from the query are in the corpus, return []
        Turn everything lowercase and ignore punctuation
        """
        order = []  # what we return; order of docs with tfidf high->low
        doc_tfidfs = {}  # {doc1: tfidf, doc2: tfidf, ...}
        query_words_unique = list(set(query.split()))

        for word in query_words_unique:  # go thru every unique word in query
            # normalize word first
            word = word.lower()
            word = re.sub(r'\W+', '', word)
            if word in self._all_unique:  # skip ones that are not in corpus
                # only the docs with word
                for doc in self._inverted_index[word]:
                    if doc not in doc_tfidfs:
                        # initialize tfidf for that word
                        doc_tfidfs[doc] = self._calculate_indiv_tfidf(word,
                                                                      doc)
                    else:
                        # tfidf for more words
                        doc_tfidfs[doc] += self._calculate_indiv_tfidf(word,
                                                                       doc)

        # sort doc_tfidfs dictionary by TF-IDF greatest->lowest
        order = sorted(doc_tfidfs.items(),
                       key=operator.itemgetter(1), reverse=True)
        # get just paths
        order = [tup[0].get_path() for index, tup in enumerate(order)]

        return order
