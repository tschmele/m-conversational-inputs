from profanity_check import predict, predict_prob

profanity2label = {1: 'profanity', 0: 'safe'}
exit_con = 'exit'

print(f'profanity check. stop by typing "{exit_con}"')
last_input = input('you: ')

while (last_input != exit_con):
    print(f'pc: your text was classified as "{profanity2label[predict([last_input])[0]]}" with a certainty of {predict_prob([last_input])[0]:.2%}')
    last_input = input('you: ')

print(f'pc: until next time!')
