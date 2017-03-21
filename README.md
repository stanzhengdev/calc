## Calculator

Parses and evaluates normal infix notation expressions like "2 + 2" ==`4`.
Supports basic calculator operators `add`, `sub`, `mult`, `div`, `exp`.

- Note supports integers and integer `floor_division`.
- Floating point PR's accepted!
- Python supports [unlimited precision][http://stackoverflow.com/questions/9860588/maximum-value-for-long-integer] Integers so doing something like (10^10^10) will attempt to compute.


### Run
```
# Tested on Python 3.6.0+ and Python 2.7
 python -m unittest calc_test.py
 python driver.py
```

### License

APACHE 2.0
