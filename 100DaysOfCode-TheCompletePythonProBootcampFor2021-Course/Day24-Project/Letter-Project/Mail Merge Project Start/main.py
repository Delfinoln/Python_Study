with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

names_stripped = []
for name in names:
    names_stripped.append(name.strip("\n"))


with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_content = letter.read()


for name in names_stripped:
    new_letter = letter_content.replace("[name]", name)
    with open("Output/ReadyToSend/letter" + name.replace(' ', ''), mode="w") as final_letter:
        final_letter.write(new_letter)

