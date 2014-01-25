weighted_random
===============

A simple library for returning a weighted random choice from a list:

Usage:

```python
from weighted_random import weighted_choice

# Alex is 10 times more likely to win than Steve
winner = weighted_choice(['Alex', 'Steve'], [10, 1])
```

A good way to demonstrate this is by running it thousands of times:

```python
winners = {'Alex': 0, 'Steve': 0}
for i in range(10000):
    winner = weighted_choice(['Alex', 'Steve'], [10, 1])
    winners[winner] += 1
    
print winners
# {'Steve': 960, 'Alex': 9040}
```
