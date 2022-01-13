# f -> formate
to_seconds = 3
name_of_unit = 'seconds'


def days_to_units(value):
    if value > 0:  # conditional check
        return value * to_seconds
    else:
        return 'invalid Input : enter only positive value.'


user_input = input("Please Type  :\n")

x = days_to_units(int(user_input))
print(x)
print(type(x))
print(hash(user_input))
