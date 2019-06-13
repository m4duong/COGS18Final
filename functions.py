import random

def get_word():
    
    """
    Get a random word from chosen category
    
    Returns
    -------
    random.choice(names).lower() : str
        A randomly chosen name from the TAs/IAs category
    random.choice(characters).lower() : str
        A randomly chosen character from the Disney characters category
    
    """
    
    while True:
        
        # Takes the user's input, makes it lowercase, and assigns it to variable category
        category = input("Choose a category (TAs/IAs, Disney characters): \n").lower()
        
        # Check if the user's input is one of the provided categories.
        # If so, randomly chose a name or character
        # If not, go back to top of while loop
        if category == "tas/ias":
            names = ["Charles",
                     "Shreenivas",
                     "Weilun",
                     "Severine",
                     "Stephen",
                     "Ahrial",
                     "Myles",
                     "Miranda",
                     "Edward"]
            
            return random.choice(names).lower()
        
        elif category == "disney characters":
            characters = ["Ariel",
                     "Mulan",
                     "Maui",
                     "Goofy",
                     "Simba",
                     "Mickey",
                     "Nemo"]
            
            return random.choice(characters).lower()
        
        else:
            print("That is not an option. Try again.")

def replace_underscore(letter, test_word, guess_word):
    
    """
    Replace corresponding underscore with correctly guessed letter.
    This code is external code from user gontajones at https://python-forum.io/Thread-Python-Hangman-Replacing-with-letters
    Parameters
    ----------
    letter : str
        The inputted letter from user
    test_word : list
        A list of the letters from randomly chosen word 
    guess_word : list
        A list of underscores for every letter in word
        
    Returns
    -------
    guess_word : list
        List of underscores gets updated with every correct letter
   
    """
    
    # For each letter in test_word (a list made up of the letters in the chosen word),
    # find its corresponding underscore and replace it with the letter.
    # An updated list with the new letter is returned.
    for c in test_word:
        
        if c == letter:
            guess_word[test_word.index(c)] = c
            test_word[test_word.index(c)] = '*'
 
    return guess_word
 
def play_hangman():

    """
    This is the main function of the project.
    
    Returns
    -------
    str
    """
    print("Hello! Welcome to Hangman!")
    
    # For word: get the random word,
    # for test_word: make a list of the letters from word, 
    # for guess_word: replace the letters in test_word with underscores.
    # Set the amount of guesses to 10
    word = get_word()
    test_word = list(word)
    guess_word = ["_" for x in test_word]
    guesses = 10

    print("The word contains " + str(len(word)) + " letters.")

    # This while loop is where the user guesses letters to figure out the word
    while True:
        
        # Join the characters (letters and underscores) and assign to variable current_word
        current_word = "".join(guess_word)
        
        # Check to see if current version of current_word matches with chosen word
        # If so, end the loop
        if current_word == word:
            break
            
        # Check if there are still underscores in guess_word and if there are more than 0 guesses
        # If so, subtract 1 from guess to indicate a new guess is occuring
        # Then ask for the user to input a letter and check if it is a single letter
        elif "_" in guess_word and guesses >= 1:
            print("You have " + str(guesses) + " more guesses.")
            guesses -= 1
            guess = input("Guess a letter: ").lower()
            
            # If the user input was a single letter, check if the input is in the chosen word
            # If so, replace_underscore will replace an underscore with the letter
            # If not, restart loop
            if len(guess) == 1:
                
                if guess in word:
                    print("Yes! \t" + str(replace_underscore(guess, test_word, guess_word)))
                
                else:
                    print("Wrong!")
            
            # If user input was not a single letter, restart loop
            else:
                print("That is not a single letter!")
        
        # If number of guesses left is 0, restart loop
        else:
            print("Sorry, you ran out of guesses!")
            break
            
    # Return chosen word
    print("The word is " + word.capitalize() + "!")