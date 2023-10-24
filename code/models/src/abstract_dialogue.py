'''
    abstract_dialogue.py -- Contains class for representing an abstract 
    dialogue
'''

from abc import ABC
from typing import List
import json


class Turn:
    """
        This class represents a turn, a user utterance and the corresponding response.
    """

    def __init__(self, utterance:str, response:str):
        self.__utterance = utterance
        self.__response = response

    @property
    def utterance(self) -> str:
        '''
            This method returns the utterance.
            :return: utterance
        '''
        return self.__utterance

    @property
    def response(self) -> str:
        '''
            This method returns the response
            :return: response
        '''
        return self.__response

    def as_json(self):
        '''
            This method returns the turn json serializable
            :return: dict
        '''
        return {'utterance': self.__utterance,
            'response': self.__response}

    def __repr__(self):
        return json.dumps(self.as_json())


class Dialogue(ABC):
    """
        Class representing an abstract dialogue consisting of an dialogue id
        and a list of turns.
    """

    def __init__(self, dialogue_id:str):
        self.__dialogue_id = dialogue_id
        self.__turns = []
        
    @property
    def dialogue_id(self) -> str:
        '''
            Returns the dialogue id
            :return: dialogue id
        '''
        return self.__dialogue_id

    @property
    def turns(self) -> List[Turn]:
        '''
            Returns the list of turns
            :return: list of turns
        '''
        if len(self.__turns) == 0:
            raise Exception("There are no turns.")
        return self.__turns

    def append_turn(self, turn:Turn):
        '''
            Method for setting the turns
        '''
        self.__turns.append(turn)

    def __repr__(self):
        return json.dumps({'id': self.__dialogue_id,
            'turns': [t.as_json() for t in self.__turns]})
