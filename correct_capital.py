import re


def correct_capital(line: str) -> bool:
    pattern = '^[A-Z]?[a-z]+$|^[A-Z]+$'
    return bool(re.search(pattern, line))

def correct_capital(line: str) -> bool:
    return line.islower() or line.isupper() or line.istitle()


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True
assert correct_capital("checkiO") == False
assert correct_capital("CHeckio") == False
assert correct_capital("checkio") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")