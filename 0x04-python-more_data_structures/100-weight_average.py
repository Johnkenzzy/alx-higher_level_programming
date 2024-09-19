#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weightxscore = sum(x[0] * x[1] for x in my_list)
    total_weight = sum(x[1] for x in my_list)
    return total_weightxscore / total_weight if total_weight != 0 else 0
