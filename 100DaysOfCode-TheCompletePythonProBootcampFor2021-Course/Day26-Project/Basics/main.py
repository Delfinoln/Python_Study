# ##### Learning list comprehension
#
# numbers = [1, 2, 3]
# new_list = [number + 1 for number in numbers]
#
# print(new_list)
#
# name = "Lucas"
# new_list = [letter for letter in name]
#
# print(new_list)
#
# list_number = range(1, 5)
# list_doubled = [number * 2 for number in list_number]
#
# print(list_doubled)


# ##### Learning conditional list comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# short_names = [name for name in names if len(name) <= 4]
#
# print(short_names)
#
# long_names = [name.upper() for name in names if len(name) > 4]
#
# print(long_names)


# ##### Create a List Comprehension to create a new list called squared_numbers.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2 for number in numbers]
#
# print(squared_numbers)


# ##### Write a list comprehension to create a new list called result. This new list should contain
# #####    the even numvers from the list numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [number for number in numbers if number % 2 == 0]
#
# print(result)


# ##### List comprehension with data reading
# with open("file1.txt") as data:
#     data1 = data.readlines()
#
# data1 = [int(data.strip()) for data in data1]
#
#
# with open("file2.txt") as data:
#     data2 = data.readlines()
#
# data2 = [int(data.strip()) for data in data2]
#
# result = [number for number in data1 if number in data2]
#
# print(result)


# ##### Dictionary comprehension
# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# scores_dictionary = {name: random.randint(0, 100) for name in names}
#
# print(scores_dictionary)
#
# passed_students = {name: scores_dictionary[name] for name in names if scores_dictionary[name] >= 60}
#
# print(passed_students)
#
# print(scores_dictionary.items())


# ##### Dictionary Comprehension to create a dictionary called result that takes each word in the
# #####     given sentence and calculates the number of letters in each word
# sentence = "What is the Airspeed Velocity of Unladen Swallow?"
# sentence_split = sentence.split()
#
# result = {word: len(word) for word in sentence_split}
#
# print(result)
