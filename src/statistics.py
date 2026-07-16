import json

def count_errors(passage,user_input):
    count=0
    for i, letter in enumerate(passage):
        for u, uletter in enumerate(user_input):
            if i==u and letter!=uletter:
                count+=1 
    return count

def calculate_wpm(user_input,elapsed_time):

    if elapsed_time<=0:
        return 0

    words = len(user_input)/5

    return int(words/elapsed_time)

def net_wpm(wpm,count,elapsed_time):

    if elapsed_time<=0:
        return 0

    uncorrect_error_wpm = count/elapsed_time

    return int(wpm-uncorrect_error_wpm)

def calculate_cpm(user_input,elapsed_time):
    
    cpm=len(user_input)/elapsed_time
    return int(cpm)

def calculate_accuracy(user_input,count):

    if len(user_input)<=0:
        return 0
    
    accuracy= (len(user_input)-count)/len(user_input)

    return accuracy*100

def save_score():
    
    with open("data/highscores.json", "r") as f:
        data = json.load(f)  

    with open ("data/history.json", "w") as f:
        json.dump(data, f, indent=4)


def load_best_score():
    pass

    