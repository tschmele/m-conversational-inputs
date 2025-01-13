import pickle

from convokit import Corpus
from convokit import download
from convokit import TextParser
from convokit import PolitenessStrategies
from convokit import Classifier


wiki_corpus = Corpus(download('wikipedia-politeness-corpus'))
parser = TextParser(verbosity=5000)
ps = PolitenessStrategies()


wiki_corpus = parser.transform(wiki_corpus)
wiki_corpus = ps.transform(wiki_corpus, markers=True)


binary_corpus = Corpus(utterances=[utt for utt in wiki_corpus.iter_utterances() if utt.meta['Binary'] != 0])


test_ids = binary_corpus.get_utterance_ids()[-100:]
train_corpus = Corpus(utterances=[utt for utt in binary_corpus.iter_utterances() if utt.id not in test_ids])
test_corpus = Corpus(utterances=[utt for utt in binary_corpus.iter_utterances() if utt.id in test_ids])
print("train size = {}, test size = {}".format(len(train_corpus.get_utterance_ids()),
                                               len(test_corpus.get_utterance_ids())))

clf = Classifier(obj_type='utterance', 
                        pred_feats=['politeness_strategies'], 
                        labeller=lambda utt: utt.meta['Binary'] == 1)
clf.fit(train_corpus)

model = clf.get_model()

with open('./convotest/model.p', 'wb') as f:
    pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
