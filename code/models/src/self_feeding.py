'''
    self_feeding.py -- This script contains the class for representing a collection of self_feeding dialogues.
'''

from typing import Dict, List
from data_augmentation_models.abstract_data_collection import DialogueCollection
from data_augmentation_models.abstract_dialogue import Dialogue, Turn

class SelfFeedingDialogue(Dialogue):
    """
        Class representing an dialogue from the self_feeding dataset
    """

    def __init__(self, dialogue_id:str, turns:List[Dict]):
        super(SelfFeedingDialogue, self).__init__(dialogue_id)

        if len(turns) > 0:
            for turn in turns:
                super().append_turn(Turn(turn[0], turn[1]))
            
            # catches the case where we have an uneven number of turns
            #if res < len(turns)-1:
            #    super().append_turn(Turn(turns[res+1]['text'], ''))

        else:
            raise Exception("Length of turns must not be 0.")

class SelfFeedingDialogueCollection(DialogueCollection):
    """
        Class for representing the hb split of the self-feeding chatbot
    """

    def __init__(self, filename:str, type:str, split:str):
        super(SelfFeedingDialogueCollection, self).__init__(filename, type, 
            split)

        for d in super().data:
            #import json
            #print(json.dumps(d))
            #exit()    
            dialogue = SelfFeedingDialogue(d['dialogue_id'], d['turns'])
            super().append_dialogue(dialogue)
