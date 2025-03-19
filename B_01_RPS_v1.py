import random

# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"please neter a valid option from the following list: {valid_ans}"

    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()

def instructions():
    """Displays instructions"""

    print("""
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
- Paper beats rock
- Rock beats scissors
- Scissors beats paper

Press <xxx> to end the game at anytime.

good luck!
    """)

def int_check(question):
    while True:
        error = "please enter a integer that is 1 or more"

        to_check = input(question )
        if to_check == "":
            return "infinite"

        try:

            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def rps_conpare(user, comp):
    print()
    print("user", user)
    print("comp", comp)

    if user == comp:
        result = "tie"

    elif user == "paper" and comp == "rock":
        result = "win"

    elif user == "scissors" and comp == "paper":
        result = "win"

    elif user == "rock" and comp == "scissors":
        result = "win"

    else:
        result = "lose"

    return result



# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock","paper", "scissors", "xxx"]

print("💎📰✂️Rock/Paper/scissors game💎📰✂️")
print()

# asks if the user wants instructions then displays the instructions if the answer is yes
want_instructions = string_checker("do you want to see the instructions? ").lower()
if want_instructions == "yes":
    instructions()

# ask for number of rounds/infinite mode
num_rounds = int_check("how many rounds would you like? or press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
# game loop starts here
while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    comp_choice = random.choice(rps_list[:-1])
    print("computer choice")

    user_choice = string_checker("choose: " , rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break



    result = rps_conpare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    #if players are in inf mode then increase the rounds
    if mode == "infinite":
        num_rounds += 1


# game loop ends

# game history/ statistics area
