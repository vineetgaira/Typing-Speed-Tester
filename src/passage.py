from pathlib import Path
import random

def load_passages(difficulty):
    pass


def random_passage():

    text = Path("passage/easy.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return random.choice(passages)


def load_category(difficulty):
    pass

def load_difficulty():
    pass