# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=['yes', 'no']):

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



#main routine goes here


rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("do you want to see the instructions?",)

print("you chose: ", want_instructions)

user_choice = string_checker("choose: ", rps_list)
print("you chose", user_choice)