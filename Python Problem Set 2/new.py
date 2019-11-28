# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:25:39 2019

@author: vicke
"""
import string


def is_word_guessed(secret_word, letters_guessed):
    """
    Takes a secret_word and a list of letters.
    Returns a boolean - True if the secret_word has been guessed. False otherwise.
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed = False
            break
        else:
            guessed = True
                    
    return guessed

def get_guessed_word(secret_word, letters_guessed):
    """
    Takes in a secret_word, and a list of letters guessed.
    Returns a string comprised of a list of letters and underscores for which letters have been guessed.
    """

    display_string = ""
    
    for letter in secret_word:
        if letter not in letters_guessed:
            display_string = display_string + "_ "
        else:
            display_string = display_string + letter + " "
            
    return display_string

def get_available_letters(letters_guessed):
    display_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            display_letters = display_letters + letter + " "
        else:
            continue
    return display_letters            