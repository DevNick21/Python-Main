
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as name:
    list_of_names = name.readlines()

main_list = []

for item in list_of_names:
    main_list.append(item.strip())

for name in main_list:
    with open("./Input/Letters/starting_letter.txt", mode= "r") as letter:
        new_letter = letter.read()
    with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode= "w") as written:
        written.write(new_letter.replace("[name]", name))