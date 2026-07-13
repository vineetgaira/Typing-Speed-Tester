from pathlib import Path
import random

def load_passages():

    text = Path("passage/easy.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return random.choice(passages)


def random_passage():
    pass

def load_category():
    pass

def load_difficulty():
    pass