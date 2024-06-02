import copy

# Lista anidada
ops = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

# Copia profunda de la lista anidada
ops_copy = copy.deepcopy(ops)

# Cambiamos un elemento en la lista original
ops[0][0] = 100

# Imprimimos la lista original y la copia
print(ops_copy)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
print(ops)  # [[100, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]