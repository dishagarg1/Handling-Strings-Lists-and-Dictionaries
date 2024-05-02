# defining the text 
def alternate_case_characters(text):
    # split the text into characters
    characters = list(text)

# iterate over the length of characters 
    for i in range(len(characters)):
        if i % 2 ==0: # even number will convert to uppercase
            characters[i] = characters[i].upper()
        else:
            characters[i] = characters[i].lower() # odd number will convert to lowercase
    
    #join the characters back into the string and return
    return' '.join(characters)

# iterate over the length of characters 
def alternate_case_words(text):
    words = text.split()

    for i in range(len(words)):
        if i % 2 ==0:   # even number will convert to uppercase
            words[i] = words[i].upper()
        else:
            words[i] = words[i].lower()  # odd number will convert to lowercase
    #join the words back into the string and return
    return' '.join(words)
        
# ask the user to enter a sentence       
input_string = input("Enter a string: ")

output_string = alternate_case_characters(input_string)
print(output_string)

output_string = alternate_case_words(input_string)
print(output_string)    
