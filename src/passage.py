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

def load_all(difficulty):

    text = Path(f"passage/difficulty/{difficulty}.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return passages

def next_passage(difficulty):

    passages=load_all(difficulty)
    pos = index_difficulty.get(difficulty, 0)

    passage=passages[pos%len(passages)]
    index_difficulty[difficulty] = pos + 1

    return passage


def reset_sequence(difficulty):

    index_difficulty[difficulty]=0
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

    passages=load_all(category)
    pos = index_category.get(category, 0)

    passage=passages[pos%len(passages)]
    index_category[category] = pos + 1

    return passage
