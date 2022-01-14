import datetime

user_input = input("Enter your goal with a deadline separated by a colon: \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = datetime.datetime.strptime(input_list[1],"%d.%m.%Y")
current_date = datetime.datetime.today()

print(f"Dear user time remaining for { goal } is {deadline - current_date}")
