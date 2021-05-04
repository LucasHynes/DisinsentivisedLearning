#uses the neuron classes and how they are able to interact with each other
import v2.neuron as neuron
import copy

N_COUNT = 100

network = [copy.copy(neuron.n) for _ in range(N_COUNT)]

def proper_index(n_no, add_val, l):
    if n_no + add_val > len(l):
        new_index = (n_no + add_val) - len(l)
        return l[new_index]
    else:
        return l[n_no + add_val]

#connects the nuerons to a mapped algo
def n_mapping(network):
    
    for n_no in range(len(network)):
        network[n_no].child1 = proper_index(n_no, 1, network)
        network[n_no].child2 = proper_index(n_no, 2, network)

    return network