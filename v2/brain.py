#uses the neuron classes and how they are able to interact with each other
import neuron
import copy

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

print(input_n.child1.c1_strength)