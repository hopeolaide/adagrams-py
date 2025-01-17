
import random
import copy 

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10

    }
def draw_letters():
    user_pool = copy.deepcopy(LETTER_POOL)
    letter_bank = [] 
    while len(letter_bank)< 10: 
        draw = random.choice(list(user_pool))
        for letter in user_pool.keys():
            if user_pool[letter] == 0:
                continue 
            if letter == draw: 
                letter_bank.append(draw) 
                user_pool[letter] -= 1 
                
    return letter_bank 

from collections import Counter 

def uses_available_letters(word, letter_bank):
    input_word = word.upper()
    print(f"This is the value of {input_word=}")
    #We initially explored using the Counter approach but didnt go with it. 
    # We left it here (commented out) to be able to discuss in our 1:1s with instructors
    # word_counter = Counter(input_word)   
    # # letter_bank_counter = Counter(letter_bank)    
 
    for letter in input_word:  
        if letter not in letter_bank:
            return False
        elif letter in letter_bank:
            word_letter_frequency = input_word.count(letter)
            letter_bank_frequency = letter_bank.count(letter)
            if word_letter_frequency > letter_bank_frequency:
                return False       
    return True

    # Remnant from initial Counter approach:
    # for (k, v), (k2, v2)  in  zip(word_counter.items(), letter_bank_counter.items()): 
    #     zip(word_counter.items(), letter_bank_counter.items()) 
    #     if k == k2 and v > v2: 
    #         return False
    #      
    # return True 

def score_word(word):
    """
Wave 3: score_word
Returns the score of a given word as defined by the Adagrams game.

The number of points of each letter is summed up to represent the total score of word
Each letter's point value is described in the table below
If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points

"""
    input_word = word.upper()
    word_score = 0
    word_length = len(input_word)

    if input_word == "":
        return 0

    for letter in input_word:
        word_score += SCORE_CHART[letter]

    if word_length >= 7: 
        word_score += 8

    return word_score
    

def get_highest_word_score(word_list):
    best_word_list = []
    best_score_list =[]

# Translating word list and scores into a dictionary and finding highest word score in dictionary:
    for word in word_list:
        word_score_dict = {word: score_word(word) for word in word_list}    #Dictionary comprehension 
        highest_word_score = max(word_score_dict.values())

# Max only returns the first match so we need to check which (if any) other values == highest score
# Once clear append the keys for those highest_scores values to the best_word_list.
    for word in word_score_dict:
        if word_score_dict[word] == highest_word_score:
            best_word_list.append(word)
            best_score_list.append(word_score_dict[word])

#Conditional check to see if length is more than 1 then apply tie-breaker logic 
# (see helper function further below)    
    best_word = best_word_list[0] if len(best_word_list) == 1 else tie_breaker(best_word_list)

    return (best_word, highest_word_score)     

#Tie-breaker logic 
def tie_breaker(best_word_list):
    for word in best_word_list:
        if len(word) == 10:
            return word
        
    return min(best_word_list, key = len) 
    



