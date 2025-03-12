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



# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

print("💎📰✂️Rock/Paper/scissors game💎📰✂️")
print()

# instructions

# ask for number of rounds/infinite mode
num_rounds = int_check("how many rounds would you like? or press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    print("you chose infinite")
    num_rounds = 5
# game loop starts here
while rounds_played < num_rounds:
    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played: ", rounds_played)

    #if players are in inf mode then increase the rounds
    if mode == "infinite":
        num_rounds += 1
    print("num of rounds: ", num_rounds)


# game loop ends

# game history/ statistics area
