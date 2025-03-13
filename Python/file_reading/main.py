#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("inputs/invited_names.txt", "r") as names:
    name_list = names.readlines()
    # print(name_list)

with open("inputs/starting_letter.txt") as file:
    file = file.read()

    for name in name_list:
        name = name.strip("\n")
        new_file = file.replace("[name]", name)
        with open(f"Output/{name}_file.txt", mode="w") as file:
                file.write(new_file)
