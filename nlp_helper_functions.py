'''
    File name: nlp_helper_functions.py
    Author: Ali Salloum & Samuli Reinikainen
    Date created: 20/08/2021
    Date last modified: 02/09/2021
    Python Version: 3.8
'''

import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.preprocessing import OneHotEncoder
import re
from wvlib_light import lwvlib
# LANGUAGE PREPROCESSING

def address_nan(iterable):
    " This function converts float(nan) to string(nan) "
    processed_iterable = ["nan" if type(e) is float else e for e in iterable]
    return processed_iterable

def remove_punctuations(iterable):
    " This function removes most of the irrelevant punctuations from the words "
    processed_iterable = [e.translate(str.maketrans('', '', string.punctuation)) for e in iterable]
    return processed_iterable

def remove_emails(iterable):
    " This function removes emails from the strings in iterable "
    processed_iterable = [re.sub(r'\S+@\S+\.\S+', "", e) for e in iterabe]
    assert len(processed_iterable) == len(iterable)
    return processed_iterable

def remove_regex(iterable, regex):
    " This function removes any regex from the strings in the iterable "
    processed_iterable = [re.sub(regex, "", e) for e in iterable]
    assert len(processed_iterable) == len(iterable)
    return processed_iterable
    
# VECTORIZATION

def one_hot_encoding(iterable, ignore_unknown = False, return_transformers = False):
    " This function creates one hot encodings for a single feature or multiple features and returns the transformer if specified "
    handle_unknown = "error"
    if ignore_unknown:
        handle_unknown = "ignore"
    ohe = OneHotEncoder(handle_unknown = handle_unknown)
    transformed = ohe.fit_transform(iterable)
    assert len(transformed) == len(iterable)
    if return_transformers:
        return transformed, transformer
    else:
        return transformed

def bag_of_words(iterable, max_features, ngram_range = (1,1), tfidf=True, return_transformers = False):
    """ 
        This function creates bag of words vectors for the iterable 
        Returns the vector-iterable and the transformers if specified
    """
    vectorizer = CountVectorizer()
    vectorized = vectorizer.fit_transform(iterable, max_features = max_features, ngram_range = ngram_range)
    transformer = None
    if tfidf:
        transformer = TfidfTransformer()
        vectorized = transformer.fit_transform(vectorized)
    assert len(vectorized) == len(iterable)
    if return_transformers:
        return vectorized, (vectorizer, transformer)
    else:
        return vectorized


class Embedding(lwvlib.WV):
    def __init__(self, filename):
        self.WV = lwvlib.load(filename, 100000, 5000000)
    def vec(self, word):
        return self.WV.w_to_normv(word)
    


if __name__=="__main__":
    print("NLP-tools imported successfully.")
