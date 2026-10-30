def tem_convert():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

    for i in range(3):
        choice = input("enter your choice: ")

        if choice == "1":
            celsius = float(input("enter temperature in celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"Temperature in Fahrenheit: {fahrenheit}")
        elif choice == "2":
            fahrenheit = float(input("enter temperature in fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"Temperature in Celsius: {celsius}")
        elif choice == "3":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        tem_convert()