def Receiving_a_number():
    number = int(input("Enter a number: "))
    if number < 0:
        print("Error: Please enter a non-negative integer.")
    
def sibit():
    sibit=int(input("Enter sibit 1-8: "))
    if sibit < 1 or sibit > 8:
        print("Error: Please enter a number between 1 and 8.")
    
def Decimal_to_binary_number(number):
    binary = format(number, '08b')
    print(binary)
