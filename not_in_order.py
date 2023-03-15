def not_order(data: list[int]) -> int:
    return len(list(filter(lambda x: x[0] != x[1], zip(data, sorted(data)))))

def not_order(data: list[int]) -> int:
    return len([a for a in zip(data, sorted(data)) if a[0] != a[1]])

print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

# assert not_order([1, 1, 4, 2, 1, 3]) == 3
# assert not_order([]) == 0
# assert not_order([1, 1, 1, 1, 1]) == 0
# assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")