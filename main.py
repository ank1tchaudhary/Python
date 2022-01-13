# f -> formate
to_seconds = 3
name_of_unit = 'seconds'


def days_to_units(value):
    return value * to_seconds


user_input = input("Please Type  :\n")

x = days_to_units(int(user_input))
print(x)
