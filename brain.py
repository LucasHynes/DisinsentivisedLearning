#uses the neuron classes and how they are able to interact with each other
import v2.neuron as neuron
import copy
from random import random
N_COUNT = 100

input_n = copy.copy(neuron.n)
check_n = copy.copy(neuron.n)
change_n = copy.copy(neuron.n)
output_n = copy.copy(neuron.n)

input_n.child1 = check_n
input_n.child2 = change_n
check_n.child1 = change_n
check_n.child2 = output_n
change_n.child1 = output_n
output_n.child1 = input_n

def decision(n1, n2):
    if random() * (n1+n2) <= n1:
        return n1
    else:
        return n2

def thought(i, ck, ch, o):
    if ((i.type != "input") or (ck.type != "check")) or ((ch.type != "type") or (o.type != "output")):
        print("WARNING: impropper type of neuron passed through the function, returning error!")
        return -1