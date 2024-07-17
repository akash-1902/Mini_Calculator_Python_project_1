class mini_calculator:
    def calculator(self):
        user_input = int(input("Enter your total number of values: "))
        values = []
        for i in range(1, user_input + 1):
            value = int(input(f"Enter your {i} value: "))
            values.append(value)
        print("Enter your choice:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = int(input("Enter your choice: "))

        result = values[0]

        if choice==1: #Addition
            for value in values[1:]:
                result+=value
            operation="Addition"

        elif choice == 2:  # Subtraction
            for value in values[1:]:
                result -= value
            operation = "Subtraction"

        elif choice == 3:  # Multiplication
            for value in values[1:]:
                result *= value
            operation = "Multiplication"

        elif choice == 4:  # Division
            for value in values[1:]:
                result /= value
            operation = "Division"

        else:
            result = "Invalid choice!"
            operation = "Invalid"
        # Displaying the result
        print(f"The result of the {operation} is: {result}")
obj=mini_calculator()
obj.calculator()
