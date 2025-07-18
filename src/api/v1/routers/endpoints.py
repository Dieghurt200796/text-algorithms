from fastapi import APIRouter, Depends, HTTPException

from .. import dependencies
from src.application.services import WordStore
from src.application import services
from ..schemas import TextInput

router = APIRouter()

@router.post("/word/", status_code=201)
def add_word(text: TextInput, store: WordStore = Depends(dependencies.get_word_store)):
    store.set_word(text.text)

@router.get("/full/")
def get_full_analysis():
    analysis = services.get_full_analysis()
    if analysis:
        return analysis
    else: raise HTTPException(status_code=404, detail="No text found.")

@router.get("/palindrome/")
def get_palindrome():
    analysis = services.get_palindrome()
    if analysis:
        return analysis
    else: raise HTTPException(status_code=404, detail="No text found.")

@router.get("/vowels/")
def get_vowels():
    analysis = services.get_letters()
    if analysis:
        return analysis
    else: raise HTTPException(status_code=404, detail="No text found.")

@router.get("/anagrams/")
def get_anagrams():
    analysis = services.get_anagrams()
    if analysis:
        return analysis
    else: raise HTTPException(status_code=404, detail="No text found.")

@router.get("/ordered/")
def get_ordered():
    analysis = services.get_ordered()
    if analysis:
        return analysis
    else: raise HTTPException(status_code=404, detail="No text found.")

@router.get("/permutations/")
def get_permutations():
    analysis = services.get_permutations()
    if analysis:
        return analysis
    else: raise HTTPException(status_code=404, detail="No text found.")