

def lattice_paths(coords):
    count = 1
    if coords[0] != 0:
        count += 1 + lattice_paths((coords[0] - 1, coords[1]))
    if coords[1] != 0:
        count += 1 + lattice_paths((coords[0], coords[1] - 1))
    print count
    return count

print lattice_paths((2, 2))
        
