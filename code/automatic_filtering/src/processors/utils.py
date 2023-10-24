'''
    This script contains some utility function for preprocessing data
    to be processed with sentence transformer
'''

import json
import os
from typing import List, Tuple, Dict
from nltk.tokenize import sent_tokenize

def chunk_pairing(phrase:str, utterance:str) ->List[Tuple[str, str]]:
    '''
        This method implements a simple pairing algorithm:
            (1) The number of words n in the phrase are evaluated (when 
                splitted by a whitespace). 
            (2) The utterance is splitted by the white space. 
            (3) Overlapping chunks of size n are built from the original 
                utterance (with n - (n - 1) overlapping token). E.g.: n = 2; 
                utterance = "This is a test" ->["This is", "is a", "a test"]
            (4) The phrase is paired with each of the chunks and this is 
                returned as list.
        :param phrase: The phrase.
        :param utterance: The utterance to chunk.
        :return: List of Tuples of the form (phrase, chunk of utterance)
    '''
    n = len(phrase.split(' '))
    _utterance = utterance.split(' ')
    chunks = [' '.join(_utterance[i:i+n]) 
        for i in range(0, len(_utterance), n - (n - 1))
        if len(_utterance[i:i+n]) == n]
    pairs = [(phrase.lower(), chunk.lower()) for chunk in chunks]

    return pairs

def sentence_pairing(phrase:str, utterance:str) ->List[Tuple[str, str]]:
    '''
        This method implements a pairing algorithm on sentence-level:
            (1) The utterance is splitted by nltk's sent_tokenizer.
            (2) Instead of using the phrases, here, the original sentences
                (the sentence that contain the phrases) are used.
            (4) The sentence of the utterance is paired with the origin sentence of the phrase.
        :param sentence: The origin sentence of the phrase (including the 
            phrase).
        :param utterance: The utterance.
        :return: List of Tuples of the form (origin sentence, sentence from 
            utterance)
    '''    
    _utterance = sent_tokenize(utterance)
    pairs = [(phrase.lower(), sent.lower()) for sent in _utterance]

    return pairs

def dump_results(results:Dict, name:str, folder:str) -> None:
    '''
        This method just dumps the result into a json file on the specified location
    '''
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(os.path.join(folder, name + '.json'), 'w', encoding='utf-8')\
        as file:
        json.dump(results, file)
