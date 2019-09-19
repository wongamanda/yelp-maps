"""Utilities for Maps"""

from math import sqrt
from random import sample

# Rename the built-in zip (http://docs.python.org/3/library/functions.html#zip)
_zip = zip

def map_and_filter(s, map_fn, filter_fn):
    """Returns a new list containing the results of calling map_fn on each
    element of sequence s for which filter_fn returns a true value.
    """
    return [map_fn(i) for i in s if filter_fn(i)]

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    """
    return min(d, key=lambda key_name: d[key_name])

def zip(*sequences):
    """Returns a list of lists, where the i-th list contains the i-th
    element from each of the argument sequences.
    """
    return list(map(list, _zip(*sequences)))

def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    """
    return list(list([i+start, s[i]]) for i in range(0, len(s)))

def distance(pos1, pos2):
    """Returns the Euclidean distance between pos1 and pos2, which are pairs.
    """
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def mean(s):
    """Returns the arithmetic mean of a sequence of numbers s.
    """
    assert s != []
    return sum(s)/len(s)    
