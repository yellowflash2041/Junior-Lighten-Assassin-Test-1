# Do NOT edit nor remove any existing code when testing or submitting
def main_function(input):
    # Place your code here
    while input >= 10:
        temp = input
        mul = 1
        while temp > 1:
            mul *= temp % 10
            temp = int(temp / 10)
        input = mul
    return input

