from pathlib import Path
import random

index_difficulty={
    1: "easy",
    2: "medium",
    3: "hard"
}

index_category={
    1: "general",
    2: "history",
    3: "literature",
    4: "programming",
    5: "quotes",
    6: "science"

}

difficulty_position={
    "easy": 0,
    "medium": 0,
    "hard": 0}

category_position={
    "general": 0,
    "history": 0,
    "literature": 0,
    "programming": 0,
    "quotes": 0,
    "science": 0}

def load_all(difficulty):

    text = Path(f"passage/difficulty/{difficulty}.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return passages

def next_passage(difficulty):

    passages=load_all(difficulty)
    pos = difficulty_position.get(difficulty, 0)

    passage=passages[pos%len(passages)]
    difficulty_position[difficulty] = pos + 1

    return passage

def random_passage(difficulty):

#This returns a random passage 
    text = Path(f"passage/{difficulty}.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return random.choice(passages)
    
def load_category(category):
# This loads all the passages for selected category
    text = Path(f"passage/category/{category}.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return passages

def category_passage(category):

    passages=load_category(category)
    pos = category_position.get(category, 0)

    passage=passages[pos%len(passages)]
    category_position[category] = pos + 1

    return passage

