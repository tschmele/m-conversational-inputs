# import convokit
import spacy

# from convokit import Corpus, Speaker, Utterance
# from convokit import download
# from convokit import TextParser

from convokit import PolitenessStrategies

ps = PolitenessStrategies()
spacy_nlp = spacy.load('en_core_web_sm', disable=['ner'])

utt = ps.transform_utterance('hello, could you please help me proofread this article?', spacy_nlp=spacy_nlp)
meta = utt.meta['politeness_strategies']

print(f'{utt.meta}')
