import pickle

from convokit import Corpus, Utterance, Speaker
from convokit import TextParser
from convokit import PolitenessStrategies
from convokit import Classifier

from better_profanity import profanity

profanity.add_censor_words(['sht', 'fck', 'fuc'])


prof2label = {1: 'profanity', 0: 'safe'}
pred2label = {1: "polite", 0: "impolite"}
speakers = ['user']
corpus_speakers = {s: Speaker(id=s, meta={}) for s in speakers}

parser = TextParser(verbosity=5000)
ps = PolitenessStrategies()
with open('convotest/model.p', 'rb') as f:
    model = pickle.load(f)
clf = Classifier(obj_type='utterance', 
                        pred_feats=['politeness_strategies'], 
                        labeller=lambda utt: utt.meta['Binary'] == 1)
clf.set_model(model)


def check_profanity(utt):
    return {
        'prediction': profanity.contains_profanity(utt)
    }


def check_politeness(utt):
    corp = Corpus(utterances=[Utterance(
            id='in',
            speaker=corpus_speakers['user'],
            text=utt,
            conversation_id='0',
            reply_to=None,
            meta={'type' : 'input'}
        )])
    parsed = parser.transform(corp)
    parsed = ps.transform(parsed)
    
    pred = clf.transform(parsed)
    return pred.get_utterance('in') # has .meta['prediction'] and .meta['pred_score']


def judge_input(utt):
    profanity = check_profanity(utt)
    politness = check_politeness(utt)

    if profanity['prediction'] == 1:        # predicted as 'offensive'
        return -3
    if politness.meta['prediction'] == 1:   # predicted as 'polite'
        return 2
    if "please" in utt.lower():
        return 1
    
    return 0