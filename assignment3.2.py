# set functions (set operations)
a={1, 2, 3, 4}
b={3, 4, 5, 6}
print(a.union(b)) # this will return a new set which is the union of set a and set b {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # this will return a new set containing only the elements that are present in both set a and set b {3, 4}
print(a.difference(b)) # this will return a new set containing only the elements that are present in set a but not in set b {1, 2}
print(a.symmetric_difference(b)) # this will return a new set containing only the elements that are present in either set a or set b but not in both {1, 2, 5, 6}
print(a.issubset(b)) # this will return True if set a is a subset of set b and False if it is not a subset of set b False
print(a.issuperset(b)) # this will return True if set a is a superset of set b and False if it is not a superset of set b False
print(a.isdisjoint(b)) # this will return True if set a and set b have no elements in common and False if they have at least one element in common False

