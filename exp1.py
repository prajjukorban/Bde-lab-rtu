def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_hex(n):
    return hex(n)[2:].upper()

def binary_to_decimal(b):
    return int(b, 2)

def hex_to_decimal(h):
    return int(h, 16)

while True:
    print("\nMenu:")
    print("1. Decimal to Binary")
    print("2. Decimal to Hexadecimal")
    print("3. Binary to Decimal")
    print("4. Hexadecimal to Decimal")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        d = int(input("Enter decimal: "))
        print("Binary:", decimal_to_binary(d))
    elif choice == '2':
        d = int(input("Enter decimal: "))
        print("Hexadecimal:", decimal_to_hex(d))
    elif choice == '3':
        b = input("Enter binary: ")
        print("Decimal:", binary_to_decimal(b))
    elif choice == '4':
        h = input("Enter hexadecimal: ")
        print("Decimal:", hex_to_decimal(h))
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")