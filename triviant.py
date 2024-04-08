import requests


def refactor_sentence(sentence):
    if '&' in sentence:
        sentence = sentence.replace('&quot;', '"').replace('&#039;', "'").replace('&amp;', '&').replace('&lt;',
                                                                                                        '<').replace(
            '&gt;', '>')
    return sentence


def get_trivia_question():
    url = "https://opentdb.com/api.php?amount=1&difficulty=easy"
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        question = response['results'][0]['question']
        question = refactor_sentence(question)

        correct_answer = response['results'][0]['correct_answer']
        incorrect_answers = response['results'][0]['incorrect_answers']
        options = incorrect_answers + [correct_answer]
        options.sort(reverse=True)
        return question, correct_answer, options
    else:
        print("Failed to retrieve question. Please wait a second.")
        return None, None, None


def display_question(question, options):
    print(refactor_sentence(question))
    i = 1
    for option in options:
        print(f"{i}. {option}")
        i += 1


def get_user_answer():
    try:
        return int(input("Enter your answer: "))
    except ValueError:
        print("Please enter a valid option number.")
        return get_user_answer()


def check_answer(user_answer, correct_answer_index):
    return user_answer == correct_answer_index


def play_game():
    input("Press Enter to get a new question...")
    question, correct_answer, options = get_trivia_question()
    if question and correct_answer and options:
        display_question(question, options)
        user_answer = get_user_answer()
        if check_answer(user_answer, options.index(correct_answer) + 1):
            print("Correct! Well done!")
        else:
            print("Incorrect! The correct answer was:", correct_answer)
            print("")
    else:
        play_game()


def main():
    print("Welcome to the Trivia Game!")
    print("Let's start!")
    play_again = True

    while play_again:
        play_game()
        print("Do you want to play another round? (yes/no)")
        response = input().lower()
        play_again = response == "yes" or response == "y"

    print("Thank you for playing!")


main()
