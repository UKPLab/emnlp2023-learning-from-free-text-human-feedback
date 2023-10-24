'''
    phrases.py -- Class for representing phrases
'''

from data_augmentation_models.abstract_data_collection import DataCollection

class Phrases(DataCollection):
    """
        Class representing phrases and offering operations on them.
    """

    def __init__(self, filename:str):
        super(Phrases, self).__init__(filename)
        