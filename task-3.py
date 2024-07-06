def check_delimiters(input_string):
    stack = []
    matching_brackets = {")": "(", "]": "[", "}": "{"}

    for char in input_string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if matching_brackets[char] != top:
                return "Несиметрично"

    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


# Приклади тестування
test_cases = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]

for test in test_cases:
    result = check_delimiters(test)
    print(f"{test}: {result}")
