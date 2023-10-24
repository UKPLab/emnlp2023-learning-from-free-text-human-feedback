'''
    data.py -- Class representing an abstract data collection.
'''

import json
from abc import ABC
from typing import List, Dict
from data_augmentation_models.abstract_dialogue import Dialogue


class DataCollection(ABC):
    """
        Class representing an abstract data collection.
    """

    def __init__(self, filename:str):
        with open(filename, 'r', encoding='utf-8') as file:
                self.__data = json.load(file)

    @property
    def data(self) -> Dict:
        '''
            Return data dictionary.
            :return: data dictionary.
        '''
        return self.__data
        

class DialogueCollection(DataCollection):
    """
        Class representing an abstract dialogue collection.
    """

    def __init__(self, filename:str, type:str, split:str):
        super(DialogueCollection, self).__init__(filename)
        self.__type = type
        self.__split = split
        self.__dialogues = []

    @property
    def type(self):
        '''
            Return the type of this dialogue collection.
            :return: type
        '''
        return self.__type

    @property
    def split(self):
        '''
            Return the split of this dialogue collection.
            :return: split
        '''
        return self.__split

    @property
    def dialogues(self) -> List[Dialogue]:
        '''
            Return list of dialogues
            :return: list of dialogues.
        '''
        return self.__dialogues

    def append_dialogue(self, dialogue:Dialogue):
        '''
            Method for appending dialogues
        '''
        self.__dialogues.append(dialogue)

    def get_utterances(self) -> Dict:
        '''
            This method returns all utterances from all dialogues of this
            dialogue collection (along with their dialogue_id)
            :return: Dict of the form {dialogue_id: [list of utterances]}
        '''

        utterances = {}
        for dialogue in self.__dialogues:
            utterances[dialogue.dialogue_id] =\
                [turn.utterance for turn in dialogue.turns]

        return utterances
