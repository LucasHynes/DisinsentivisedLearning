from typing import NoReturn
import neuron
import pathTracker
import knowledgeBase

# The point to test will be a code given to the computer as four characters before and after some number of opperations
# of the given tools to find a computer generated algorithm to build itself an algo for the answer. 


NEURON_COUNT = 20
BASE_NEURON_STRENGTH = 0.05

n_list = [neuron.neuron for i in range(NEURON_COUNT)]

#used to input the material to test the learning functions
def input_data_function():
    return None

#the base functions availiable to the robot to solve the problem
def learning_tools():
    return None

#enviorment to allow for the interaction of data and computer
def testing_enviorment():
    
    data_in = input_data_function()
    expected = "AFHC"
    tools = learning_tools()

    #initialize the neurons with base strength None data
    for n in n_list:
        for n1 in n.connections:
            n[n1] = BASE_NEURON_STRENGTH

    test_answer([], data_in, expected)

    return None

#control for how the computer "reacts" to the data to turn it into better mapped brain
def learn_control():
    return None

def memory():
    return None

def neuron_memory():
    return None

def disincentivise(n1, n2):
    n1[n2] *= 0.8
    n2[n1] *= 0.8

def incentivise(n1, n2):
    n1[n2] *= 1.2
    n2[n1] *= 1.2

def switcher(arg, in):
    switch = {
        1:knowledgeBase.tool_1(in),
        2:knowledgeBase.tool_2(in)
    }
    return switch.get(arg, "tool not found")

def test_answer(path, input, expectedOutput):
    #go through logic to confirm the result of the current path
    for n in path:
        if n.function_access_num  > 0:
            input = switcher(n.function_access_num, input)
    
    return (input != expectedOutput)

def percent_off(attempt, expected):
    num_char_off = 0

    if len(attempt) == len(expected):
        for i in range(len(attempt)):
            if attempt[i] != expected[i]:
                num_char_off *= (abs(ord(attempt[i]) - ord(expected[i])))/26

    return num_char_off