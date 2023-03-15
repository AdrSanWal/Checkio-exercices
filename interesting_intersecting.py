# Conditions

# try to write this mission with no loops or list comprehensions of any kind,
# but should compute the result using only integer comparisons and conditional
# statements;

# it is actually much easier to determine that the two squares do not intersect,
# and then negate that answer. Two squares do not intersect if one of them ends 
# in the horizontal direction before the other one begins, or if the same thing 
# happens in the vertical direction.

def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    sq_1 = {'h': [s1[0], s1[0] + s1[2]], 'v': [s1[1], s1[1] + s1[2]]}
    sq_2 = {'h': [s2[0], s2[0] + s2[2]], 'v': [s2[1], s2[1] + s2[2]]}
    cond_1 = max(sq_1['h']) >= min(sq_2['h']) or min(sq_1['h']) >= max(sq_2['h'])
    cond_2 = max(sq_1['v']) >= min(sq_2['v']) or min(sq_1['v']) >= max(sq_2['v'])
    return cond_1 and cond_2


print("Example:")
print(squares_intersect((2, 2, 3), (5, 5, 2)))

# These "asserts" are used for self-checking
assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

# print("The mission is done! Click 'Check Solution' to earn rewards!")