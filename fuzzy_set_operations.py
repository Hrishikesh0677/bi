# Fuzzy Set Operations and Relations

print("\n--- Fuzzy Set Operations ---")

# Define fuzzy sets
A = {'a': 0.7, 'b': 0.5, 'c': 0.2}
B = {'a': 0.4, 'b': 0.6, 'c': 0.9}

# Union
union = {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

# Intersection
intersection = {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

# Complement of A
complement_A = {x: 1 - A[x] for x in A}

# Difference A - B
difference = {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in A}

# Print operations
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Union A ∪ B:", union)
print("Intersection A ∩ B:", intersection)
print("Complement of A:", complement_A)
print("Difference A - B:", difference)

print("\n--- Fuzzy Relation (Cartesian Product) ---")

# Define fuzzy sets for relation
X = {'x1': 0.5, 'x2': 0.8}
Y = {'y1': 0.6, 'y2': 0.3}

# Cartesian Product (Fuzzy Relation)
relation = {}
for x in X:
    for y in Y:
        relation[(x, y)] = min(X[x], Y[y])

# Print fuzzy relation
for pair, value in relation.items():
    print(f"{pair}: {value}")

print("\n--- Max-Min Composition ---")

# Define two fuzzy relations R and S
R = {
    ('x1', 'y1'): 0.5, ('x1', 'y2'): 0.3,
    ('x2', 'y1'): 0.6, ('x2', 'y2'): 0.3
}

S = {
    ('y1', 'z1'): 0.7, ('y1', 'z2'): 0.2,
    ('y2', 'z1'): 0.4, ('y2', 'z2'): 0.9
}

# Perform Max-Min Composition: R o S
Z = {}
for x in ['x1', 'x2']:
    for z in ['z1', 'z2']:
        min_vals = []
        for y in ['y1', 'y2']:
            min_vals.append(min(R.get((x, y), 0), S.get((y, z), 0)))
        Z[(x, z)] = max(min_vals)

# Print result of Max-Min Composition
for pair, value in Z.items():
    print(f"{pair}: {value}")
