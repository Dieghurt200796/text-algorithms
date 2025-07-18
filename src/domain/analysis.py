import string
from pathlib import Path



def is_palindrome(text : str) -> bool:
    return text==text[::-1]

def letter_count(text : str) -> dict:
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    num_consonants = 0

    for c in text.lower():
        if c in string.ascii_lowercase:
            if c in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return {
        'vowels': num_vowels,
        'consonants': num_consonants
    }

def anagram(text : str) -> list:
    current_file_path = Path(__file__)
    project_root = current_file_path.parent.parent.parent
    file_path = project_root / "resources" / "words.txt"

    text = text.lower()
    anagrams = []

    with open(file_path, 'r') as f:
        words = f.read().lower().split("\n")
        for word in words:
            if len(word) == len(text):
                if sorted(word) == sorted(text) and word != text:
                    anagrams.append(word)

    return anagrams

def order_alphabetically(text : str) -> str:
    ordered = sorted(text.lower())
    output = ""
    for letter in ordered:
        output += letter

    return output

def permutations_algorithm(text : list, perms: list = None, current_permutation : str = '') -> list:
    if perms == None:
        perms = []

    for letter in text:
        current_permutation += letter
        new_text = text.copy()
        new_text.remove(letter)
        if new_text:
            permutations_algorithm(new_text, perms, current_permutation)
        else:
            perms.append(current_permutation)
        current_permutation = current_permutation[:-1]
    return perms

def permutations(text : str) -> set:
    text = list(text)
    perms = set(permutations_algorithm(text))
    return perms



