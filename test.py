from __future__ import division
from weighted_random import weighted_choice
from collections import defaultdict


# Test simple 1 to 10
results = defaultdict(int)

for i in range(100000):
    x = weighted_choice(['apple', 'banana'], [1, 10])
    results[x] += 1

print results

print results['banana'] / results['apple']

# Test several
results = defaultdict(int)

for i in range(100000):
    x = weighted_choice(
        ['fish', 'banana', 'apple', 'nandos'],
        [1, 10, 100, 15]
    )
    results[x] += 1

print results

print results['apple'] / results['fish']
print results['banana'] / results['fish']
print results['nandos'] / results['fish']

# Test 50 50
results = defaultdict(int)

for i in range(100000):
    x = weighted_choice(['apple', 'banana'], [1, 1])
    results[x] += 1

print results

print results['banana'] / results['apple']
