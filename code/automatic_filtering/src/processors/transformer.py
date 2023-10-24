'''
    transformer.py -- Contains code for working with sentence-transformer 
    library.
'''

from typing import List, Tuple, Dict
from sentence_transformers import SentenceTransformer, util
from tfd_models.phrases import Phrases
from tfd_models.abstract_data_collection import DialogueCollection
from processors.utils import chunk_pairing, sentence_pairing
from tqdm import tqdm


class SentenceTransformerWrapper:
    """
        Class for working with sentence-transformer library.
    """

    def __init__(self, pairing:str, model_name:str='all-mpnet-base-v2'):
        self.__model = SentenceTransformer(model_name)
        self.__pairing = pairing

    def calc_sim(self, pairs:List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        '''
            Method for calculating the cosine similarity between the phrases
            of two lists of strings.
            :param phrases_1: First list.
            :param phrases_2: Second list.
            :return: List of tuples consisting of (phrase_1, phrase_2, score)
                in reversed order
        '''

        strs_1 = [pair[0] for pair in pairs]
        strs_2 = [pair[1] for pair in pairs]

        #Compute embedding for both lists
        embeds_1 = self.__model.encode(strs_1, convert_to_tensor=True, batch_size=256)
        embeds_2 = self.__model.encode(strs_2, convert_to_tensor=True, batch_size=256)

        #Compute cosine-similarities
        scores = util.cos_sim(embeds_1, embeds_2)
        scores = [(str_1, str_2, round(scores[i][i].item(), 3))
            for i, (str_1, str_2)
            in enumerate(zip(strs_1, strs_2))]
        # scores = sorted(scores, key=lambda x: x[2], reverse=True)
        return scores

    def process(self, phrases:Phrases, data:DialogueCollection) -> Dict:
        results = {}

        print('\n')
        print(f'Processing {str(type(data))}')

        for k, v in tqdm(data.get_utterances().items()):
            results[k] = []
            pairs = []
            for phrase in phrases.data:
                for ut in v:
                    pair = chunk_pairing(phrase, ut)\
                        if self.__pairing == 'chunk'\
                        else sentence_pairing(phrase, ut)                    
                    if len(pair) > 0:
                        pairs += pair
            # if the utterance is smaller than the phrase, pairs might 
            # be empty
            results[k] += self.calc_sim(pairs)

        return results
