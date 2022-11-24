import random

bet = 10
lucky_number = random.randint(1, 5)
print()
print(f'Generated lucky number is: {lucky_number}\n')


def casino(my_number):
    if my_number == 0:
        return 'Make bet greater then 0'
    elif my_number <= 5:
        return f'Your bet is {my_number} and you win is double {my_number*2}, total summ is {my_number*2+lucky_number}'
    else:
        return f'Make bet equal or less then 5'


def validate_and_execute():
    try:
        my_input_number = int(my_input)
        bet_value = casino(my_input_number)
        print(bet_value)
    except:
        print('Make a number bet !!!')


my_input = ''
while my_input != 'no':
    my_input = input('If you want to play make your lucky bet, if not say: "no"\n')
    validate_and_execute()

