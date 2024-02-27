import os
from pathlib import Path

# Determine the correct path to the file
file_path = Path("C:/Users/myi2/Documents/GitHub/oim3640/Sessions 11/words.text")

def find_long_words():
    """
    Prints only the words with more than 20 characters.
    """
    with file_path.open() as f:
        for line in f:
            word = line.strip()
            if len(word) > 20:
                print(word, len(word))

def has_no_e(word):
    """
    Returns True if the given word doesn't have the letter 'e' in it.
    """
    return "e" not in word.lower()

def find_words_no_e():
    """
    Returns the percentage of the words that don't have the letter 'e'.
    """
    total_words = 0
    words_no_e = 0
    with file_path.open() as f:
        for line in f:
            word = line.strip()
            total_words += 1
            if has_no_e(word):
                words_no_e += 1
    return (words_no_e / total_words) * 100 if total_words > 0 else 0

def avoids(word, forbidden):
    """
    Returns True if the given word does not use any of the forbidden letters.
    """
    return not any(letter in forbidden for letter in word.lower())

def find_words_no_vowels():
    """
    Returns the percentage of the words that don't have vowel letters.
    """
    vowels = "aeiou"
    total_words = 0
    words_no_vowel = 0
    with file_path.open() as f:
        for line in f:
            word = line.strip()
            total_words += 1
            if avoids(word, vowels):
                words_no_vowel += 1
    return (words_no_vowel / total_words) * 100 if total_words > 0 else 0

def uses_only(word, available):
    """
    Takes a word and a string of letters, and returns True if the word
    contains only letters in the string available.
    """
    return set(word.lower()).issubset(set(available.lower()))

def find_words_only_use_planet():
    letters = "planets"
    count = 0
    with file_path.open() as f:
        for line in f:
            word = line.strip()
            if uses_only(word, letters):
                count += 1
    return count

def uses_all(word, required):
    """
    Takes a word and a string of required letters, and returns True if
    the word uses all the required letters at least once.
    """
    return set(required.lower()).issubset(set(word.lower()))

def find_words_using_all_vowels():
    vowels = "aeiou"
    count = 0
    with file_path.open() as f:
        for line in f:
            word = line.strip()
            if uses_all(word, vowels):
                count += 1
    return count

def is_abecedarian(word):
    """
    Returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    return all(word[i] <= word[i+1] for i in range(len(word)-1))

def find_abecedarian_words():
    count = 0
    with file_path.open() as f:
        for line in f:
            word = line.strip()
            if is_abecedarian(word):
                count += 1
    return count

if __name__ == "__main__":
    print("Long words with more than 20 characters:")
    find_long_words()

    perc_no_e = find_words_no_e()
    print(f'\nThe percentage of the words with no "e" is {perc_no_e:.2f}%.')

    perc_no_vowel = find_words_no_vowels()
    print(f'\nThe percentage of the words without vowel letters is {perc_no_vowel:.2f}%.')

    print("\nNumber of words that use only letters from 'planets':", find_words_only_use_planet())

    print('\nThe number of words that use all the vowels:', find_words_using_all_vowels())

    print('\nThe number of abecedarian words:', find_abecedarian_words())
