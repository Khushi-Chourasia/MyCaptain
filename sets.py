a = input("Enter elements for set A separated by commas: ")
A = set(a.split(','))

b = input("Enter elements for set B separated by commas: ")
B = set(b.split(','))

# Union
union = A.union(B)
print("Union of E and N is", union)

# Intersection
intersection = A.intersection(B)
print("Intersection of E and N is", intersection)

# Difference
difference = A.difference(B)
print("Difference of E and N is", difference)

# Symmetric Difference
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference of E and N is", symmetric_difference)