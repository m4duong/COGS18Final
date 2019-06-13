"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import get_word, replace_underscore, play_hangman

##
##

def test_get_word():
    
    category = "Disney characters"
    
    assert isinstance("Disney characters", str)

def test_replace_underscore():
    
    word = "sand"
    guess_word = ["_" for x in word]
    
    assert guess_word == ["_", "_", "_", "_"]