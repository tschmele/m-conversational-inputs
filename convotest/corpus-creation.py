import convokit
import spacy

from convokit import Corpus, Speaker, Utterance
from convokit import download
from convokit import TextParser

speakers = ['user', 'pc']

corpus_speakers = {s: Speaker(id=s, meta={}) for s in speakers}

# utts = [input(), '']

# if (utts[0] == 'ping'):
#     utts[1] = 'pong'
# else:
#     utts[1] = 'you had to say "ping"'
# print(f'{utts[1]}')

# corpus_utterances = {
#     'u0': Utterance(id='u0', speaker=corpus_speakers['user'], conversation_id='c0', text=utts[0], meta={}),
#     'u1': Utterance(id='u1', speaker=corpus_speakers['pc'], conversation_id='c0', text=utts[1], reply_to='u0', meta={})
# }

last_input = ''
exit_con = 'exit'
corpus_utterances = {}
i = 0

print(f'type "{exit_con}" to stop this madness')
corpus_utterances['u'+str(i)] = Utterance(id='u'+str(i), speaker=corpus_speakers['pc'], text='type "' + exit_con + '" to stop this madness', conversation_id='c0', reply_to=None, meta={'type' : 'info'})
i += 1
while (last_input != exit_con):
    last_input = input('you : ')
    if (last_input == exit_con):
        corpus_utterances['u'+str(i)] = Utterance(id='u'+str(i), speaker=corpus_speakers['user'], text=last_input, conversation_id='c0', reply_to='u'+str(i-1), meta={'type' : 'exit'})
        i += 1
    else:
        corpus_utterances['u'+str(i)] = Utterance(id='u'+str(i), speaker=corpus_speakers['user'], text=last_input, conversation_id='c0', reply_to='u'+str(i-1), meta={'type' : 'input'})
        i += 1

        if (last_input == 'ping'):
            res = 'pong'
        else:
            res = 'you had to say "ping"'
        print(f'pc : {res}')
        corpus_utterances['u'+str(i)] = Utterance(id='u'+str(i), speaker=corpus_speakers['pc'], text=res, conversation_id='c0', reply_to='u'+str(i-1), meta={'type' : 'response'})
        i += 1

utterance_list = corpus_utterances.values()
corpus = Corpus(utterances=utterance_list)

corpus.print_summary_stats()
convo = corpus.get_conversation('c0')
convo.print_conversation_structure(lambda utt: utt.speaker.id + ' : ' + utt.text[:80])
