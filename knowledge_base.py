import string
def tool_one(input):
    return input.reverse()

def score(attempt, answer):

    if not (isinstance(attempt, list)):
        return "Error: Attempt var is not type list!"
    
    if not (isinstance(answer, list)):
        return "Error: Answer var is not type list"

    if len(attempt) != len(answer):
        return "Error: Length of the answers attempted to score have different lengths"

    return percent_off(attempt, answer)

def percent_off(attempt, expected):
    num_char_off = 0.000
    if len(attempt) == len(expected):
        for i in range(len(attempt)):
            if attempt[i] != expected[i]:
                num_char_off += (letters_off(attempt[i], expected[i])/13 * (1/len(attempt)))

    return num_char_off

def letters_off(char_1, char_2):
    char_1 = char_1.upper()
    char_2 = char_2.upper()
    alphabet = list(string.ascii_uppercase)
    reverse = alphabet[::-1]

    if char_1 < char_2:
        reverse_length = alphabet.index(char_1) + 1 + reverse.index(char_2)
        length = alphabet.index(char_2) - alphabet.index(char_1)
    else:
        reverse_length = alphabet.index(char_2) + 1 + reverse.index(char_1)
        length = alphabet.index(char_1) - alphabet.index(char_2)  
    
    return min(reverse_length, length)

