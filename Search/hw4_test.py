"""
Avery Lee
CSE 163 AB
This program implements the testings for HW Search.
Search inputs a string query and returns a list of documents that
is the best search for that query in descending order.
Documents with higher TF-IDF scores are considered to be better searches.

This file implements testing for all required
functions in search_engine.py and document.py
including term_frequency(), get_path(), get_words(), _calculate_idf(), search()
"""

from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine
import math
import os


# Define your test functions here!
# Testing document.py
def test_term_frequency(doc1, doc2, doc3):
    """
    Tests the term_frequency method
    """
    assert_equals(1/4, doc1.term_frequency('class'))
    assert_equals(1/4, doc2.term_frequency('and'))
    assert_equals(2/7, doc3.term_frequency('best'))


def test_get_path(doc1, doc2, doc3):
    """
    Tests the get_path method
    """
    assert_equals('/home/docs/doc1.txt', doc1.get_path())
    assert_equals('/home/docs/doc2.txt', doc2.get_path())
    assert_equals('/home/docs/doc3.txt', doc3.get_path())


def test_get_words(doc1, doc2, doc3):
    """
    Tests the get_words method
    """
    # sorted() to keep it consistent when testing
    assert_equals(['i', 'love', 'this', 'class'],
                  doc1.get_words())
    assert_equals(['hi', 'andrea', 'and', 'wen'],
                  doc2.get_words())
    assert_equals(['you', 'are', 'best', 'and', 'tas', 'ever'],
                  doc3.get_words())


# Testing search_engine.py
def test__calculate_idf(se):
    """
    Tests the _calculate_idf method
    """
    assert_equals(math.log(3/1), se._calculate_idf('love'))
    assert_equals(math.log(3/1), se._calculate_idf('best'))
    assert_equals(math.log(3/2), se._calculate_idf('and'))


def test_search(se, doc1, doc2, doc3):
    """
    Tests the search method
    """
    # none
    assert_equals([], se.search('hello there'))
    # 'andrea' in doc2
    assert_equals(['/home/docs/doc2.txt'], se.search('hElLo anDRea!'))
    # assert_equals([(doc2, (1/4)*math.log(3/1))], se.search('hello anDRea!'))
    # # 'and' in doc2+3, 'best' in doc3
    assert_equals(['/home/docs/doc3.txt', '/home/docs/doc2.txt'],
                  se.search('anD. best'))


def main():
    """
    Main function
    """
    directory = '/home/docs/'  # the corpus
    # when I use a for loop to append the doc objects,
    # it appends them out of order. was told to just
    # hard code it inside
    doc1 = Document(os.path.join(directory, 'doc1.txt'))
    doc2 = Document(os.path.join(directory, 'doc2.txt'))
    doc3 = Document(os.path.join(directory, 'doc3.txt'))

    # document.py test
    print(test_term_frequency(doc1, doc2, doc3))
    print(test_get_path(doc1, doc2, doc3))
    print(test_get_words(doc1, doc2, doc3))

    # search_engine.py test
    se = SearchEngine(directory)
    print(test__calculate_idf(se))
    print(test_search(se, doc1, doc2, doc3))


if __name__ == '__main__':
    main()
