#uses the neuron classes and how they are able to interact with each other
import neuron
import copy
from random import random
N_COUNT = 100

input_n = neuron.n("input")
check_n = neuron.n("check")
change_n = neuron.n("change")
output_n = neuron.n("output")

input_n.child1 = check_n
input_n.child2 = change_n
check_n.child1 = change_n
check_n.child2 = output_n
change_n.child1 = output_n
output_n.child1 = input_n

algo_access = -1


def thought(i):

    active_n = i
    ck = i.child1
    ch = i.child2
    o = ck.child2
    if ((i.type != "input") or (ck.type != "check")) or ((ch.type != "change") or (o.type != "output")):
        print("WARNING: impropper type of neuron passed through the function, returning error!")
        return -1

    if i.play == False:
        active_n = ck.decision()
        
        if active_n.type == "change":
            active_n = ck.child1
        else:
            active_n = ck.child2

thought(input_n)