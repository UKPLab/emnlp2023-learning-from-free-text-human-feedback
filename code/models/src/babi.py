'''
    babi.py -- This script contains the class for representing a collection of BABI dialogues.
'''

from typing import Dict, List
from data_augmentation_models.abstract_data_collection import DialogueCollection
from data_augmentation_models.abstract_dialogue import Dialogue, Turn

class BabiDialogue(Dialogue):
    """
        Class representing an BABI dialogue
    """

    def __init__(self, dialogue_id:str, turns:List[Dict]):
        super(BabiDialogue, self).__init__(dialogue_id)

        if len(turns) > 0:
            for turn in turns:
                if len(turn) > 1:
                    super().append_turn(Turn(turn[0], turn[1]))
            
            # catches the case where we have an uneven number of turns
            #if res < len(turns)-1:
            #    super().append_turn(Turn(turns[res+1]['text'], ''))

        else:
            raise Exception("Length of turns must not be 0.")

class BabiCollection(DialogueCollection):
    """
        Class for representing PersonaChat
    """

    def __init__(self, filename:str, type:str, split:str, task:str):
        super(BabiCollection, self).__init__(filename, type, split)

        self.__task = task

        for d in super().data:        
            #import json
            #print(json.dumps(d))
            #exit()    
            dialogue = BabiDialogue(d['dialogue_id'], d['turns'])
            super().append_dialogue(dialogue)

    @property
    def task(self):
        '''
            return value for task
        '''
        return self.__task