# Pounds to kg
def poundsToKg():
    while True:
        try:
            toConvert = float(input("Enter your weight in pounds: "))
            break
        except ValueError:
            print("Input not accepted. Please only put digits!")
    print(f"Your weight in kg is {round(toConvert * float(0.454))}")

def kgToPounds():
    while True:
        try:
            toConvert = float(input("Enter your weight in kg: "))
            break
        except ValueError:
            print("Input not accepted. Please only put digits!")
    print(f"Your weight in pounds is {(round(toConvert * float(2.205)))}")

if __name__ == "__main__":
    print("Calculator:")
    print("1. Pounds to kg")
    print("2. Kg to pounds")
    selection = input("Please select a number: ")
    while True:
        try:
            if(selection == str(1)):
                poundsToKg()
                break
            elif(selection == str(2)):
                kgToPounds()
                break
        except ValueError:
            print("Not a valid input! Please select an option by inputting the digit.")
