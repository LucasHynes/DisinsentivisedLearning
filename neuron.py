import random
import knowledgeBase
class n:
    connections = {}
    data = None
    function_access_num = -1
    
    def find_likely(self):
        sum_strength = 0.0
        for k,v in self.connections:
            sum_strength+=v

        counter = 0.0
        rand = random() * sum_strength
        i = 0
        for k,v in self.connections:
            i += 1
            if(counter + v) < rand:
                counter += v
            else:
                return k,i      