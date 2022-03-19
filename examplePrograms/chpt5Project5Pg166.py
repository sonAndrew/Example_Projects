# Lookup Table
binaryToDecimalTable = {
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def repToDecimal(string, integer):
    # Variables
    decimal = 0
    exponent = len(string) - 1

    for digit in string:
        decimal = decimal + int(digit) * integer ** exponent
        exponent = exponent - 1
    print("The integer value is", decimal)

# Main Function
def main():
    # Variables
    bitString = input("Enter a string of bits: ")
    baseInteger = int(input("Enter an integer: "))
    repToDecimal(bitString, baseInteger)

if __name__ == '__main__':
    main()















# Function that converts binary to decimal
# def repToDecimal(string, integer):
#     decimal = 0
#     exponent = len(string) - 1
#     for digit in binaryToDecimal:
#         decimal = decimal + int(digit[integer]) * integer ** exponent
#         exponent = exponent - 1
#     print("The integer value is", decimal)

# repToDecimal(bitString, baseInteger)