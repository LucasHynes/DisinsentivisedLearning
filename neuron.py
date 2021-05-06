from random import random
import knowledge_base as kb
class n:

    def __init__(self, c1 = None, c2 = None, c1_strength = 1, c2_strength = 2, fun_acc = -1, data = ""):
        
        self.child1 = c1
        self.child2 = c2
        self.c1_strength = c1_strength
        self.c2_strength = c2_strength
        self.function_access = fun_acc
        self.data = data

class input(n):
    
    def input(self, i):
        self.function_access = i

class check(n):

    def decision(self):
        if random() * (self.c1_strength + self.c2_strength) <= self.c1_strength:
            return self.child1
        else:
            return self.child2

class change(n):

    def change_input(self):
        self.output = kb.tool_one(self.data)

