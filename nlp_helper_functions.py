'''
    File name: nlp_helper_functions.py
    Author: Ali Salloum & Samuli Reinikainen
    Date created: 20/08/2021
    Date last modified: 20/08/2021
    Python Version: 3.8
'''

import string

# LANGUAGE PREPROCESSING

def address_nan(iterable):
    " This function converts float(nan) to string(nan) "
    processed_iterable = ["nan" if type(e) is float else e for e in iterable]
    return processed_iterable

def remove_punctuations(iterable):
    " This function removes most of the irrelevant punctuations from the words "
    processed_iterable = [e.translate(str.maketrans('', '', string.punctuation)) for e in iterable]
    return processed_iterable

# VECTORIZATION

def one_hot_encoding():
    pass

def bag_of_words(tfidf=True):
    pass

def word_embedding():
    pass



if __name__=="__main__":
    print("NLP-tools imported successfully.")
