# from profanity_check import predict, predict_prob

# profanity2label = {1: 'profanity', 0: 'safe'}
# exit_con = 'exit'

# print(f'profanity check. stop by typing "{exit_con}"')
# last_input = input('you: ')

# while (last_input != exit_con):
#     print(f'pc: your text was classified as "{profanity2label[predict([last_input])[0]]}" with a certainty of {predict_prob([last_input])[0]:.2%}')
#     last_input = input('you: ')

# print(f'pc: until next time!')

from better_profanity import profanity

profanity.add_censor_words(['sht', 'fck', 'fuc'])

if __name__ == "__main__":
    stop = False

    print('go')

    while not stop:
        dt = input()

        if dt == 'stop':
            stop = True
            continue

        print(f'{profanity.contains_profanity(dt)}')
    
    print('stopped')