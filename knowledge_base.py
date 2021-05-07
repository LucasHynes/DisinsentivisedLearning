def tool_one(input):
    return input.reverse()

def score(attempt, answer):

    if not (isinstance(attempt, list)):
        return "Attempt var is not type list!"
    
    if not (isinstance(answer, list)):
        return "Answer var is not type list"

    if len(attempt) != len(answer):
        return "Error: length of the answers attempted to score have different lengths"