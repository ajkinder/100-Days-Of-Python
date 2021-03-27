# Higher Lower Game
# Guess which search terms are favored on the Internet

import random
from art import logo, vs
from game_data import data
#from replit import clear


def get_random_person():
    return random.choice(data)


def format_data(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'


def game():
    print(logo)
    streak = 0
    should_continue = True

    person_B = get_random_person()
    while should_continue:

        person_A = person_B
        person_B = get_random_person()
        while person_A == person_B:
            person_B = get_random_person()

        print(f"Compare A: {format_data(person_A)}.")
        print(vs)
        print(f"Against B: {format_data(person_B)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        #clear()
        #print(logo)
        is_correct = check_answer(guess, person_A['follower_count'], person_B['follower_count'])
        if is_correct:
            streak += 1
            print(f"You're right! Your current score is: {streak}")
            person_A = person_B
        else:
            print(f"Sorry, that's wrong. Final score: {streak}")
            should_continue = False


game()