"""
Avery Lee
CSE 163 AB
This program implements the Document class for HW Search.
HW Search inputs a string query and returns a list of documents that
is the best search for that query in descending order.
Documents with higher TF-IDF scores are considered to be better searches.
"""


import re


class Document:
    """
    Document class receives a single document and performs analyses
    such as getting the unique words, all words,
    and term frequency of each word
    """
    def __init__(self, doc_path):
        """
        Parameter: path of single document
        Initializes doc path, list of all words,
        doc length (number of non-unique words), list of unique words,
        dictionary of term frequency
        """
        # parameter doc_path is str
        self._doc_path = doc_path
        # list of all words
        self._all_words = self._all_words()
        # number of non-unique
        self._doc_length = len(self._all_words)
        # dictionary of term frequency for each term {term: term freq (float)}
        self._term_freq_dict = self._term_frequency_dict()
        # list of all unique words in doc
        # keys are unique
        self._unique_words = list(self._term_freq_dict.keys())

    # my own
    def _term_frequency_dict(self):
        """
        Parameter: self
        Returns dictionary {term(str): term frequency(float)} of all unique
        Special case: if no unique words, return {}
        """
        term_freq_dictionary = {}  # {term: term frequency in float}
        for word in self._all_words:
            if word not in term_freq_dictionary:
                term_freq_dictionary[word] = (float(
                                              self._all_words.count(word))
                                              / self._doc_length)
        return term_freq_dictionary

    # my own
    def _all_words(self):
        """
        Parameter: self
        Returns a list of all the non-unique (normalized) words
        Special case: if no words in doc, return []
        """
        all_words = []
        with open(self._doc_path) as f:
            lines = f.readlines()  # list of each line
            for line in lines:
                line = line.split()  # split by whitespace (even \n)
                for word in line:
                    # normalize word first
                    word = word.lower()
                    word = re.sub(r'\W+', '', word)
                    # don't add if word is blank after normalization
                    if word != '':
                        all_words.append(word)
        return all_words

    # required
    def term_frequency(self, term):
        """
        Parameter: self, term (str)
        Returns the term frequency of a given word
        Special case: if word not in doc, return 0
        Also turn everything lowercase and ignore punctuation
        """
        # normalize word first
        term = term.lower()
        term = re.sub(r'\W+', '', term)
        if term in self._term_freq_dict:
            return self._term_freq_dict[term]
        else:
            return 0

    # required
    def get_path(self):
        """
        Parameter: self
        Returns the document path provided
        """
        return self._doc_path

    # required
    def get_words(self):
        """
        Parameter: self
        Returns a list of unique (normalized) words
        """
        return self._unique_words
