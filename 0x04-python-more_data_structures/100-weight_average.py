def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_weight_score += score * weight
        total_weight += weight

    return total_weight_score / total_weight
