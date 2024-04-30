import random
import prompt


def even_odd():
    prompt.PROMPT = ''
    hidden_number = random.randint(0, 1000)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {hidden_number}')
    answer = prompt.string(prompt=None, empty=False)
    print(f'Your answer: {answer}')
    if hidden_number % 2 == 0 and answer == 'yes':
        print('Correct!')
        return True
    elif hidden_number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    elif hidden_number % 2 == 0 and answer == 'no':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
        return False