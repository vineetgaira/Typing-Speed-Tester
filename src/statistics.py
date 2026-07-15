import json

def count_errors(passage,user_input):
    count=0
    for i, letter in enumerate(passage):
        for u, uletter in enumerate(user_input):
            if i==u and letter!=uletter:
                count+=1 
    return count

def calculate_wpm(passage,elapsed_time):

    words = len(passage)/5

    return words/elapsed_time

def net_wpm(wpm,count,elapsed_time):

    uncorrect_error_wpm = count/elapsed_time

    return wpm-uncorrect_error_wpm

def calculate_cpm(passage,elapsed_time):
    
    return len(passage)/elapsed_time

def calculate_accuracy(passage,count):
    
    return (len(passage)/count)*100

def save_score():
    
    with open("data/highscores.json", "r") as f:
        data = json.load(f)  

    with open ("data/history.json", "w") as f:
        json.dump(data, f, indent=4)


def load_best_score():
    pass

    