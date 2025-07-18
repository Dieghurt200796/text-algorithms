from typing import Optional

from src.domain import analysis


class WordStore:
    def __init__(self):
        self._current_word: Optional[str] = None

    def set_word(self, new_word: str):
        self._current_word = new_word

    def get_word(self) -> Optional[str]:
        return self._current_word

# Create a single instance of the store that the whole application will share.
word_store = WordStore()


def get_full_analysis():
    text = word_store.get_word()
    if text:

        return {
            "text": text,
            "palindrome": analysis.is_palindrome(text),
            "vowels": analysis.letter_count(text)["vowels"],
            "consonants": analysis.letter_count(text)["consonants"],
            "alphabetically": analysis.order_alphabetically(text),
            "permutations": analysis.permutations(text),
        }
    else:
        return None

def get_palindrome():
    text = word_store.get_word()
    if text:
        return {
            "text": text,
            "palindrome": analysis.is_palindrome(text)
        }
    else:
        return None

def get_letters():
    text = word_store.get_word()
    if text:
        return {
            "text": text,
            "vowels": analysis.letter_count(text)["vowels"],
            "consonants": analysis.letter_count(text)["consonants"],
        }
    else:
        return None

def get_anagrams():
    text = word_store.get_word()
    if text:
        return {
            "text": text,
            "anagrams": analysis.anagram(text)
        }
    else:
        return None

def get_ordered():
    text = word_store.get_word()
    if text:
        return {
            "text": text,
            "ordered text": analysis.order_alphabetically(text)
        }
    else:
        return None

def get_permutations():
    text = word_store.get_word()
    if text:
        return {
            "text": text,
            "permutations": analysis.permutations(text)
        }
    else:
        return None

