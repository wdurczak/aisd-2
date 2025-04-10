import random

def generate_sorted_data(n):
    return sorted(random.sample(range(0, n * 10), n))