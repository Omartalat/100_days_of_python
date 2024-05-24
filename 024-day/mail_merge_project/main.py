#!/usr/bin/python3
"""
TODO: Create a letter using starting_letter.txt 
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".
    
Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
"""


# step 1: create list of names
invited_names = []
with open("./input/names/invited_names.txt") as names:
    for name in names:
        invited_names.append(name.strip())
    print(invited_names)

# step 3: create different files for each name

for i in range(len(invited_names)):

    # step 2: Replace the [name] placeholder with the actual name

    with open("./input/letters/starting_letter.txt", mode="r+") as f:
        f.readline().replace("[name]", invited_names[i])