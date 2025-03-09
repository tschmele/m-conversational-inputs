import pickle

from convokit import Corpus, Utterance, Speaker
from convokit import TextParser
from convokit import PolitenessStrategies
from convokit import Classifier

parser = TextParser(verbosity=5000)
ps = PolitenessStrategies()
with open('./convotest/model.p', 'rb') as f:
    model = pickle.load(f)
clf = Classifier(obj_type='utterance', 
                        pred_feats=['politeness_strategies'], 
                        labeller=lambda utt: utt.meta['Binary'] == 1)
clf.set_model(model)

pred2label = {1: "polite", 0: "impolite"}

speakers = ['user', 'pc']
corpus_speakers = {s: Speaker(id=s, meta={}) for s in speakers}

exit_con = 'exit'

utt_i = 0
corp = Corpus(utterances=[Utterance(id=str(utt_i), speaker=corpus_speakers['pc'], text=f'type "{exit_con}" to stop', conversation_id='0', reply_to=None, meta={'type' : 'info'})])
print(f'{corp.get_utterance(str(utt_i)).get_speaker().id}: {corp.get_utterance(str(utt_i)).text}')

last_input = input('you: ')
utt_i += 1
corp.add_utterances([Utterance(id=str(utt_i), speaker=corpus_speakers['user'], text=last_input, reply_to=str(utt_i - 1), meta={'type': 'input'})])
while (last_input != exit_con):
    parsed = parser.transform(corp)
    parsed = ps.transform(corp)

    pred = clf.transform(parsed)
    p = pred.get_utterance(str(utt_i))
    utt_i += 1
    corp.add_utterances([Utterance(id=str(utt_i), speaker=corpus_speakers['pc'], text=f'estimated input as "{pred2label[p.meta['prediction']]}" with {p.meta['pred_score']:.2%} certainty', conversation_id='0', reply_to=str(utt_i - 1), meta={'type' : 'response'})])
    print(f'{corp.get_utterance(str(utt_i)).get_speaker().id}: {corp.get_utterance(str(utt_i)).text}')

    last_input = input('you: ')
    utt_i += 1
    corp.add_utterances([Utterance(id=str(utt_i), speaker=corpus_speakers['user'], text=last_input, reply_to=str(utt_i - 1), meta={'type': 'input'})])

print(f'pc: until next time!')