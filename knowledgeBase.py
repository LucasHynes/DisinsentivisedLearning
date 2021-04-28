def tool_1(input):
    print(input)
    #assuming input is 4 char list i.e. ['A','B','C','D']
    return [input[3], input[1], input[2], input[0]]

def tool_2(input):
    if input[0] != 'Z':
        return [chr(ord(input[0])+1), input[1], input[2], input[3]]
    else:
        return ['A', input[1], input[2], input[3]]

def tool_3(input):
    if input[0] != 'A':
        return [chr(ord(input[0])-1), input[1], input[2], input[3]]
    else:
        return ['Z', input[1], input[2], input[3]]

def tool_4(input):
    return [input[2], input[3], input[0], input[1]]

def tool_5(input):
    return [input[3], input[0], input[1], input[2]]