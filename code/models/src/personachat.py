'''
    personachat.py -- This script contains the class for representing a collection of PersonaChat dialogues.
'''

from typing import Dict, List
from data_augmentation_models.abstract_data_collection import DialogueCollection
from data_augmentation_models.abstract_dialogue import Dialogue, Turn

class PersonaChatDialogue(Dialogue):
    """
        Class representing an PersonaChat dialogue
    """

    def __init__(self, dialogue_id:str, turns:List[Dict]):
        super(PersonaChatDialogue, self).__init__(dialogue_id)

        if len(turns) > 0:
            for turn in turns:
                super().append_turn(Turn(turn[0], turn[1]))
            
            # catches the case where we have an uneven number of turns
            #if res < len(turns)-1:
            #    super().append_turn(Turn(turns[res+1]['text'], ''))

        else:
            raise Exception("Length of turns must not be 0.")

class PersonaChatCollection(DialogueCollection):
    """
        Class for representing PersonaChat
    """

    def __init__(self, filename:str, type:str, split:str):
        super(PersonaChatCollection, self).__init__(filename, type, split)

        for d in super().data:        
            #import json
            #print(json.dumps(d))
            #exit()    
            dialogue = PersonaChatDialogue(d['dialogue_id'], d['turns'])

            if 'original' in filename:
                self.__appendix = '_original'
            elif 'revised' in filename:
                self.__appendix = '_revised'
            else:
                self.__appendix = ''

            super().append_dialogue(dialogue)

    @property
    def appendix(self):
        '''
            return value of appendix
        '''
        return self.__appendix                            
