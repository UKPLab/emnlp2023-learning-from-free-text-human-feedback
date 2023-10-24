'''
    main.py -- Main class for Textual Feedback Detection.
'''

import sqlite3 as os, yaml, cmd
from tfd_models.personachat import PersonaChatCollection
from tfd_models.self_feeding import SelfFeedingDialogueCollection
from tfd_models.sgd import SGDCollection
from tfd_models.wow import WoWCollection
from tfd_models.multiwoz import MultiWoZCollection
from tfd_models.babi import BabiCollection
from tfd_models.phrases import Phrases
from tfd_models.utils import create_dataset
from processors.transformer import SentenceTransformerWrapper
from processors.utils import dump_results
from typing import Dict

class TFD(cmd.Cmd):
    """
        Main class For Textual Feedback Detection.
    """

    intro = 'Welcome to the Textual Feedback Detection! \n\n'\
        + 'Commands: \n'\
        + '(1) Textual Feedback Detection: "tfd" \n'\
        + 'The command will be executed based on the configuration in the config file. \n'
    prompt = '(tfd) '

    def __init__(self, config_file:str):
        super(TFD, self).__init__()
        with open(config_file, 'r', encoding='utf-8') as file:
            self.__config = yaml.load(file, Loader=yaml.SafeLoader)

    def do_tfd(self, args:Dict) -> None:
        '''
            Method for doing tfd.
            :param args: not used (but needed based on the cmd api)
            :return: None
        '''
        #transformer = SentenceTransformerWrapper(self.__config['pairing'],
        #    self.__config['model_name'])
        #phrases = Phrases(self.__config['phrases']
        #    if self.__config['pairing'] == 'chunk'
        #    else self.__config['sentences'])

        counter = {}
        print(self.__config['datasets'])
        for dataset in create_dataset(self.__config['datasets']):

            if type(dataset) not in counter.keys():
                counter[type(dataset)] = [len(dataset.dialogues)]
            else:
                counter[type(dataset)].append(len(dataset.dialogues))
            
            #results = transformer.process(phrases, dataset)

            #for k, v in results.items():
            #    results[k] = [res for res in v
            #    if res[2] > self.__config['threshold']]

            #results_filename = name + '_' + split + '_' +\
            #    file.split('.json')[0]
            #dump_results(results, results_filename,
            #    self.__config['results'])

        for k in counter.keys():
            print(k, sum(counter[k]))

if __name__ == "__main__":
    data_augmentation = TFD('../config/config.yml')
    data_augmentation.cmdloop()    
