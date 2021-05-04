#uses the neuron classes and how they are able to interact with each other
import v2.neuron as neuron
import copy

N_COUNT = 100

network = [copy.copy(neuron.n) for _ in range(N_COUNT)]

def proper_index(n_no, add_val, l):
    if n_no + add_val > len(l):
        new_index = (n_no + add_val) - len(l)
        return l[new_index]
    elif n_no + add_val < 0:
        r_l = (copy.deepcopy(l)).reverse()
        new_index = abs(n_no + add_val)
        return r_l[new_index]
    else:
        return l[n_no + add_val]




def n_mapping(network):
    
    head_node = network[0]
    head_node.child1 = network[1]
    head_node.child2 = network[2]
    head_node.parent = network[-1]
    head_node.grandParent = network[-2]

    for n_no in range(len(network)):
        network[n_no].child1 = proper_index(n_no, 1, network)
        network[n_no].child2 = proper_index(n_no, 2, network)
        network[n_no].parent = proper_index(n_no,-1, network)
        network[n_no].grandParent = proper_index(n_no,-2, network)

    return network