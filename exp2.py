def bin_add(b1,b2):
    n1 = int(b1,2)
    n2 = int(b2,2)
    result = n1 + n2
    return bin(result)[2:]

def bin_sub(b1,b2):
    n1 = int(b1,2)
    n2 = int(b2,2)
    result = n1 - n2
    return bin(result)[2:]

def bin_multi(b1,b2):
    n1 = int(b1,2)
    n2 = int(b2,2)
    result = n1 * n2
    return bin(result)[2:]

def bin_div(b1,b2):
    n1 = int(b1,2)
    n2 = int(b2,2)
    result = n1 / n2
    return bin(result)[2:]

while True:
    b1 = input("Enter your 1st bin no:")
    b2 = input("Enter your 2nd bin no:")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplaction")
    print("4.Division")
    print("5.Exit")
    choice = input("Enter your Choice:")
    if choice=='1':
        print(f"your result is {bin_add(b1,b2)}")
    elif choice=='2':
        print(f"your result is {bin_sub(b1,b2)}")
    elif choice=='3':
        print(f"your result is {bin_multi(b1,b2)}")
    elif choice=='4':
        print(f"your result is {bin_div(b1,b2)}")
    elif choice=='5':
        break
    else:
        print("Enter a valid choice (1-5)!!!")

print("Thank you for using!!")