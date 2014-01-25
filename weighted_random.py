import random


def weighted_choice(sequence, weights):
    x = random.randint(1, sum(weights))

    accumulative_weight = 0
    for result, weight in zip(sequence, weights):
        accumulative_weight += weight
        if x <= accumulative_weight:
            return result
