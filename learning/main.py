# f -> formate
import logging
import os

to_seconds = 3
name_of_unit = 'seconds'


def days_to_units(value):
    print(value * to_seconds)


def validate_input(value):
    try:

        days_to_units(int(value))

    except:
        print('invalid Input : enter only positive non-decimal digits.')


# validate_input()

# x = ""
# while x != "exit":
#     x = input("Please Type  :\n")
#     for element in x.split(","):
#         validate_input(element)
#
#


logger = logging.getLogger("main")
logger.warning("Hi this is test")
