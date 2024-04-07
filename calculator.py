#! /usr/bin/env python3
    
def display_menu(menu_items):
    
    print("Menu:")
    for index, item in enumerate(menu_items, start=1):
        print(f"{index}. {item}")
    print("0. Exit")


def get_choice(menu_items):
    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice < 0 or choice > len(menu_items):
                print("Invalid choice. Please enter a valid option.")
            else:
                return choice
        except ValueError:
            print("Invalid choice. Please enter a valid option.")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def perform_operation(operator):
    numbers = []
    while True:
        user_input = input(f"Enter a number to {operator} (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        if user_input.isdigit():
            numbers.append(int(user_input))
        else:
            print("Invalid input. Please enter a number or 'done' to finish.")

    if numbers:
        if operator == 'add':
            result = sum(numbers)
        elif operator == 'subtract':
            result = numbers[0] - sum(numbers[1:])
        elif operator == 'multiply':
            result = 1
            for num in numbers:
                result *= num
        elif operator == 'divide':
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("Cannot divide by zero.")
                    return
                result /= num
        elif operator == 'power':
            result = numbers[0]
            for num in numbers[1:]:
                result **= num
        elif operator == 'modulo':
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("Cannot perform modulo by zero.")
                    return
                result %= num

        print(f"The result of {operator} is: {result}")

        
        if is_prime(result):
            print("The result is a prime number.")
        else:
            print("The result is not a prime number.")

        
        if result % 2 == 0:
            print("The result is even.")
        else:
            print("The result is odd.")

       
        if result % 5 == 0:
            print("The result is divisible by 5 without a remainder.")
            input("Press Enter to continue...")
        else:
            print("The result is not divisible by 5 without a remainder.")
            input("Press Enter to continue...")

    else:
        print("No numbers were entered.")
        input("Press Enter to continue...")
    
        
def main():
    menu_items = ["Add", "Subtract", "Multiply" , "Divide" , "Power of" , "Modulos"]

    while True:
        display_menu(menu_items)
        choice = get_choice(menu_items)

        if choice == 1:
            perform_operation('add')
        elif choice == 2:
            perform_operation('subtract')
        elif choice == 3:
            perform_operation('multiply')
        elif choice == 4:
            perform_operation('divide')
        elif choice == 5:
            perform_operation('power')
        elif choice == 6:
            perform_operation('modulo')
        elif choice == 0:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()
