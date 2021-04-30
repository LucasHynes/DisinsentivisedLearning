import random
import string
import neuron as ne
import knowledgeBase
import neural_map
import copy

# The point to test will be a code given to the computer as four characters before and after some number of opperations
# of the given tools to find a computer generated algorithm to build itself an algo for the answer. 


NEURON_COUNT = 5
BASE_NEURON_STRENGTH = 5
NUM_RUN = 100
RUN_NO = 75
RUN_COUNT = 0
TENTICLE_COUNT = 4
SEARCHING_LENGTH = 3
n_list = [ne.neuron(i) for i in range(NEURON_COUNT+1)]

def id_generator(size=4, chars=string.ascii_uppercase):
    return [random.choice(chars) for _ in range(size)]

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

#used to input the material to test the learning functions
def input_data_function():
    return id_generator()

#the base functions availiable to the robot to solve the problem
def learning_tools():
    return None

#enviorment to allow for the interaction of data and computer
def testing_enviorment():
    input = input_data_function()
    expected = ['A', 'F', 'M', 'C']
    global RUN_COUNT
    #initialize the neurons with base strength None data
    brain_strength_lookup = neural_map.datafile

    brain_strength_lookup = [[float(i) for i in d] for d in brain_strength_lookup]

    new_b = []
    for b in brain_strength_lookup:
        if b != []:
            new_b.append(b)

    brain_strength_lookup = new_b
    #represents head neuron w/ empty connections
    path = [n_list[0]]
    previous_score = 1.01 #default set to 101% off
    
    
    while (previous_score > 0) and (RUN_COUNT < RUN_NO):

        tenticles = [copy.copy(path) for _ in range(TENTICLE_COUNT)]
        temp_score = [0 for _ in range(TENTICLE_COUNT)]
        count = 0
        for attempt in tenticles:

            
            for i in range(SEARCHING_LENGTH):
                temp_path = copy.copy(attempt)
                temp_path.append(get_next_tool(path[-1], brain_strength_lookup))

                pct_temp = percent_off(test_answer(temp_path, input), expected)
                pct =  percent_off(test_answer(attempt, input), expected)

                if pct_temp < pct:
                    previous_score = pct_temp
                    attempt = temp_path
                    incentivise(attempt[-2], attempt[-1], brain_strength_lookup)      
                else:
                    disincentivise(temp_path[-1], attempt[-1], brain_strength_lookup)
                    
                RUN_COUNT +=1
            
            temp_score[count] = (previous_score)
            count += 1
            
        path = tenticles[temp_score.index(max(temp_score))]


    print(percent_off(test_answer(path, input), expected))
    print(brain_strength_lookup)
    neural_map.write_to_csv(brain_strength_lookup)
    return "Solved"

#control for how the computer "reacts" to the data to turn it into better mapped brain
def learn_control():
    return None

def memory():
    return None

def neuron_memory():
    return None

def disincentivise(n1, n2, brainpath):
    brainpath[n1.function_access_num][n2.function_access_num] *= 0.98
    brainpath[n2.function_access_num][n1.function_access_num] *= 0.98
    return brainpath

def incentivise(n1, n2, brainpath):
    brainpath[n1.function_access_num][n2.function_access_num] *= 1.02
    brainpath[n2.function_access_num][n1.function_access_num] *= 1.02
    return brainpath

def switcher(arg, input, path):
    switch = {
        1:knowledgeBase.tool_1(input),
        2:knowledgeBase.tool_2(input),
        3:knowledgeBase.tool_3(input),
        4:knowledgeBase.tool_4(input),
        5:knowledgeBase.tool_5(input),
        6:knowledgeBase.tool_6(path)
    }
    return switch.get(arg, "tool not found")

def test_answer(path, input):

    #go through logic to confirm the result of the current path
    for n in path:
        if (n.function_access_num  > 0) and (n.function_access_num != 6):
            new_input = switcher(n.function_access_num, input, path)
            input = new_input
        elif(n.function_access_num == 6):
            new_path = switcher(n.function_access_num, input, path)
            path = new_path
    if input != None:
        return input
    else:
        return "None input"

def percent_off(attempt, expected):
    num_char_off = 0.000
    if len(attempt) == len(expected):
        for i in range(len(attempt)):
            if attempt[i] != expected[i]:
                num_char_off += (letters_off(attempt[i], expected[i])/13 * (1/len(attempt)))

    return num_char_off

def get_next_tool(active_neuron, brain_strength_lookup):
    total_n_c_strength = 0
    for neuron in n_list:
        total_n_c_strength += brain_strength_lookup[active_neuron.function_access_num][neuron.function_access_num]
        
    finder = random.random()*total_n_c_strength
    temp = 0
    for neuron in n_list:
        
        if temp < finder:
            temp += brain_strength_lookup[active_neuron.function_access_num][neuron.function_access_num]
        else:
            return neuron

    #default to return last one if there is fault in the random/weighted algo
    return n_list[-1]

def track(path, n_next):
    if path.length > 0:
        if find_connection(path[-1], n_next):
            #if connection is found the matched strength and is added to the path
            path.append([n_next, path[-1][n_next]])

def find_connection(n1, n2):
    data = None
    
    if n1.connections.has_key(n2):
        #gets strength of connection
        data = n1[n2]
    else:
        return False
    if n2.connections.has_key(n1):
        #checks the strength for data integrity
        if data!= n2:
            print("No matched data found")
            return None
        
        return True
    else:    
        return False

for i in range(NUM_RUN):
    testing_enviorment()