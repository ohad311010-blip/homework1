def Receiving_a_number():
    number = int(input("Enter a number: "))
    if number < 0:
        print("Error: Please enter a non-negative integer.")
    return number

def bits():
    binary=int(input("Enter sibit number: "))
    if binary < 1 or binary > 8:
        print("Error: Please enter a number between 1 and 8.")
    return binary

def Decimal_to_binary_number(number, binary):
    binary1 = format(number, f'0{binary}b')
    print(binary1)

def to_twos_complement(number , binary):
    if number>= 0:
        return format(number, f'0{binary}b')
    else:
        return format((1 << binary) +number, f'0{binary}b')

if __name__ == "__main__":
    number = Receiving_a_number()
    binary = bits()
    Decimal_to_binary_number(number, binary)
    print(to_twos_complement(number, binary))
    
