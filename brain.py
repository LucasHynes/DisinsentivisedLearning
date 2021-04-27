from random import random
from typing import NoReturn
import neuron as ne
import pathTracker
import knowledgeBase

# The point to test will be a code given to the computer as four characters before and after some number of opperations
# of the given tools to find a computer generated algorithm to build itself an algo for the answer. 


NEURON_COUNT = 20
BASE_NEURON_STRENGTH = 0.05

n_list = [ne.neuron(i) for i in range(NEURON_COUNT)]

#used to input the material to test the learning functions
def input_data_function():
    return None

#the base functions availiable to the robot to solve the problem
def learning_tools():
    return None

#enviorment to allow for the interaction of data and computer
def testing_enviorment():
    
    input = input_data_function()
    expected = "AFHC"

    #initialize the neurons with base strength None data
    brain_strength_lookup = [[BASE_NEURON_STRENGTH for i in range(len(NEURON_COUNT))] for j in range(len(NEURON_COUNT))]

    #represents head neuron w/ empty connections
    path = [n_list[random.randint(0, len(n_list))]]

    previous_score = 1.01 #default set to 101% off
    ans = "AAAA"

    while previous_score > 0:

        temp_path = path
        temp_path.append(get_next_tool(path[-1], brain_strength_lookup))

        pct_temp = percent_off(test_answer(temp_path, input), expected)
        pct =  percent_off(test_answer(path, input), expected)

        if pct_temp < pct:
            previous_score = pct
            path = temp_path
            incentivise(path[-2], path[-1], brain_strength_lookup)
        else:
            disincentivise(temp_path[-1], path[-1], brain_strength_lookup)

    return "Solved"

#control for how the computer "reacts" to the data to turn it into better mapped brain
def learn_control():
    return None

def memory():
    return None

def neuron_memory():
    return None

def disincentivise(n1, n2, brainpath):
    brainpath[n1.function_access_num][n2.function_access_num] *= 0.8
    brainpath[n2.function_access_num][n1.function_access_num] *= 0.8
    return brainpath

def incentivise(n1, n2, brainpath):
    brainpath[n1.function_access_num][n2.function_access_num] *= 1.2
    brainpath[n2.function_access_num][n1.function_access_num] *= 1.2
    return brainpath

def switcher(arg, in):
    switch = {
        1:knowledgeBase.tool_1(in),
        2:knowledgeBase.tool_2(in)
    }
    return switch.get(arg, "tool not found")

def test_answer(path, input):

    #goes for initial check
    if path[0].connections.isEmpty():
        return input

    #go through logic to confirm the result of the current path
    for n in path:
        if n.function_access_num  > 0:
            input = switcher(n.function_access_num, input)
    
    return input

def percent_off(attempt, expected):
    num_char_off = 0

    if len(attempt) == len(expected):
        for i in range(len(attempt)):
            if attempt[i] != expected[i]:
                num_char_off += ((abs(ord(attempt[i]) - ord(expected[i])))/13)*0.25 #25% of the percent off of the letter

    return num_char_off

def get_next_tool(active_neuron, brain_strength_lookup):
    total_n_c_strength = 0
    for neuron in n_list:
        total_n_c_strength += brain_strength_lookup[active_neuron.function_access_num][neuron.function_access_num]
        
    finder = random()*total_n_c_strength
    temp = 0
    for neuron in n_list:
        if temp < finder:
            temp += brain_strength_lookup[active_neuron.function_access_num][neuron.function_access_num]
        else:
            return neuron

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