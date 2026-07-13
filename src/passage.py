from pathlib import Path
import random

_index={}

def load_all(difficulty="hard"):

    text = Path(f"passage/{difficulty}.txt").read_text(encoding="utf-8")
    passages = text.split("\n\n")

    return passages

def next_passage(difficulty="hard"):
    passages=load_all(difficulty)
    pos = _index.get(difficulty, 0)

    passage=passages[pos%len(passages)]
    _index[difficulty] = pos + 1

    return passage


def reset_sequence(difficulty="hard"):

    _index[difficulty]=0

def random_passage():
    pass


def load_category(difficulty):
    pass

def load_difficulty():
    pass