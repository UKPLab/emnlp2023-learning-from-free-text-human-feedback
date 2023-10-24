from typing import Dict
import os
from data_augmentation_models.self_feeding import SelfFeedingDialogueCollection
from data_augmentation_models.sgd import SGDCollection
from data_augmentation_models.personachat import PersonaChatCollection
from data_augmentation_models.wow import WoWCollection
from data_augmentation_models.multiwoz import MultiWoZCollection
from data_augmentation_models.babi import BabiCollection

def create_dataset(params:Dict):
    for name, paths in params.items():
        for split, path in paths.items():
            print(split)
            for file in os.listdir(path):
                if file.endswith('.json'):
                    if name == 'self_feeding':
                        dataset =\
                            SelfFeedingDialogueCollection(os.path.join(path, file), 'self_feeding', split)
                    if name == 'sgd':
                        dataset = SGDCollection(os.path.join(path, file), 
                            'sgd', split)
                    if name == 'personachat':
                        dataset =\
                            PersonaChatCollection(os.path.join(path, file),
                                'personachat', split)
                    if name == 'wow':
                        dataset = WoWCollection(os.path.join(path, file),
                            'wow', split)
                    if name == 'multiwoz':
                        dataset =\
                            MultiWoZCollection(os.path.join(path, file),
                                'multiwoz', split)
                    if name == 'babi':
                        task = file.split('-')[2]
                        dataset = BabiCollection(os.path.join(path, file),
                            'babi', split, task)
                    
                    yield dataset
