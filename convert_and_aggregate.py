def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    sol = {}
    for item in data:
        sol[item[0]] = sol.get(item[0], 0) + item[1]
    sol = {x: y for x, y in sol.items() if y != 0 and x != ''}
    return sol


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

# print("The mission is done! Click 'Check Solution' to earn rewards!")