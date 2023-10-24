'''
    wow.py -- This script contains the class for representing a collection of "Wizards of Wikipedia" dialogues.
'''

from typing import Dict, List
from data_augmentation_models.abstract_data_collection import DialogueCollection
from data_augmentation_models.abstract_dialogue import Dialogue, Turn

class WoWDialogue(Dialogue):
    """
        Class representing an "Wizards of Wikipedia" dialogue
    """

    def __init__(self, dialogue_id:str, turns:List[Dict]):
        super(WoWDialogue, self).__init__(dialogue_id)

        if len(turns) > 0:                
            for (ut, res) in\
                zip(list(range(0, len(turns), 2)), 
                    list(range(1, len(turns), 2))):
                super().append_turn(Turn(turns[ut]['text'],
                    turns[res]['text']))
            
            # catches the case where we have an uneven number of turns
            if res < len(turns)-1:
                super().append_turn(Turn(turns[res+1]['text'], ''))

        else:
            raise Exception("Length of turns must not be 0.")

class WoWCollection(DialogueCollection):
    """
        Class for representing MultiWoZ
    """

    def __init__(self, filename:str, type:str, split:str):
        super(WoWCollection, self).__init__(filename, type, split)

        for d in super().data:        
            #import json
            #print(json.dumps(d))
            #exit()    
            dialogue = WoWDialogue(d['dialogue_id'], d['dialog'])

            if 'random' in filename:
                self.__appendix = '_random'
            elif 'topic' in filename:
                self.__appendix = '_topic'
            else:
                self.__appendix = ''

            super().append_dialogue(dialogue)

    @property
    def appendix(self):
        '''
            return value of appendix
        '''
        return self.__appendix


