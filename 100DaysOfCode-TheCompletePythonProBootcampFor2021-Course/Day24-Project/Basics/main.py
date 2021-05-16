# ##### Reading a file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


# ##### Reading a file with "with"
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# ##### Writing a file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


##### Creating new file
with open("new_file.txt", mode="w") as new_file:
    new_file.write("Is it a new file?")