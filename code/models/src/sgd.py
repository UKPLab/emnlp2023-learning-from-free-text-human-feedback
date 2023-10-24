'''
    multiwoz.py -- This script contains the class for representing a collection of SGD dialogues
'''

from typing import Dict, List
from data_augmentation_models.abstract_data_collection import DialogueCollection
from data_augmentation_models.abstract_dialogue import Dialogue, Turn

class SGDDialogue(Dialogue):
    """
        Class representing an SGD dialogue
    """

    def __init__(self, dialogue_id:str, turns:List[Dict]):
        super(SGDDialogue, self).__init__(dialogue_id)

        if len(turns) > 0:                
            for (ut, res) in\
                zip(list(range(0, len(turns), 2)), 
                    list(range(1, len(turns), 2))):
                super().append_turn(Turn(turns[ut]['utterance'],
                    turns[res]['utterance']))
            
            # catches the case where we have an uneven number of turns
            if res < len(turns)-1:
                super().append_turn(Turn(turns[res+1]['utterance'], ''))

        else:
            raise Exception("Length of turns must not be 0.")

class SGDCollection(DialogueCollection):
    """
        Class for representing MultiWoZ
    """

    def __init__(self, filename:str, type:str, split:str):
        super(SGDCollection, self).__init__(filename, type, split)

        counter = 0
        for d in super().data:
            if 'dialogue_id' in d:
                dialogue = SGDDialogue(d['dialogue_id'], d['turns'])
                super().append_dialogue(dialogue)
            else:
                counter += 1
                print(counter, filename)
