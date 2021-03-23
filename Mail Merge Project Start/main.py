#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    for name in names:
        formatted_name = name.strip("\n")
        with open("Input/Letters/starting_letter.txt") as letter_start:
            letter = letter_start.read()
            letter_finish = letter.replace("[name]", formatted_name)
            with open(f"Output/ReadyToSend/letter_for_{formatted_name}.txt", mode='w') as new_file:
                new_file.write(letter_finish)







# with open(f'../Mail Merge Project Start/Output/ReadyToSend/{name}.text', mode='w') as file:
#     pass



