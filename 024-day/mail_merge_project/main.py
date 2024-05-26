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
PLACEHOLDER = "[name]"


# step 1: create list of names
with open("./input/names/invited_names.txt") as f:
    names = f.readlines()

# step 3: create different files for each name

for name in names:

    # step 2: Replace the [name] placeholder with the actual name

    with open("./input/letters/starting_letter.txt", mode="r+") as f:
        old_letter = f.read()
        new_letter = old_letter.replace(PLACEHOLDER, name.strip())
        with open(f"./output/readytosend/{name.strip()}.txt", mode="w") as file:
            file.write(new_letter)