print("What you want to calculate")
print("""
*Voltage(V)
*Current(I)
*Resistance(R)
*Power(W)
""")
print("Please respect capital letters!")
cin1 = input()


match cin1:
    case "V":
        current = input("Enter the current: ")
        resistance = input("Enter the resistance: ")

        print("Voltage is: " + str(int(current)*int(resistance)))
    case "I":
        voltage = input("Enter the voltage: ")
        resistance = input("Enter the resistance: ")

        print("Current is: " + str(int(voltage)/int(resistance)))
    case "R":
        current = input("Enter the current: ")
        voltage = input("Enter the voltage: ")

        print("Resistance is: " + str(int(voltage)/int(current)))
    case "W":
        current = input("Enter the current: ")
        voltage = input("Enter the voltage: ")

        print("Power is: " + str(int(voltage)*int(current)))
    case _:
        print("enter a valid option")
