import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = list()
        for key,value in args.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, number_to_draw):
        withdrawals = list()
        if number_to_draw > len(self.contents):
            for ball in self.contents:
                withdrawals.append(ball)
            self.contents=[]
            return withdrawals
        else:
            while number_to_draw > 0:
                index_to_remove = random.randint(0, len(self.contents)-1)
                withdrawals.append(self.contents[index_to_remove])
                self.contents.pop(index_to_remove)
                number_to_draw-=1
            return withdrawals
        
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0

    while num_experiments > 0:
        experiment_copy = copy.deepcopy(hat)
        histogram = dict()
        drawn_balls = experiment_copy.draw(num_balls_drawn)
        for ball in drawn_balls:
            histogram[ball] = histogram.get(ball, 0) + 1

        for key,value in expected_balls.items():
            if key not in histogram:
                break
            if value > histogram[key]:
                break
        else:
            M += 1

        num_experiments-=1
    return M/N
