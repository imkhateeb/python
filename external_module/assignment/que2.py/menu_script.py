# main_program.py

import var_mod as vm

def calculate_contr():
    """ Function to calculate the control variable """
    return vm.a + 10 * vm.b * vm.c - 5 * vm.d / vm.e

def initialize_variables():
    """ Function to initialize variables """
    vm.a = float(input("Enter value for a: "))
    vm.b = float(input("Enter value for b: "))
    vm.c = float(input("Enter value for c: "))
    vm.d = float(input("Enter value for d: "))
    vm.e = float(input("Enter value for e: "))

def show_variables():
    """ Function to display the current values of the variables """
    print(f"a = {vm.a}, b = {vm.b}, c = {vm.c}, d = {vm.d}, e = {vm.e}")

def modify_variables():
    """ Function to modify a specific variable """
    var_name = input("Enter the variable name to modify (a, b, c, d, e): ")
    if var_name in ['a', 'b', 'c', 'd', 'e']:
        new_value = float(input(f"Enter new value for {var_name}: "))
        setattr(vm, var_name, new_value)
    else:
        print("Invalid variable name.")

def main():
    while True:
        print("\nMenu:")
        print("1. Initialize Variables")
        print("2. Show Variables")
        print("3. Modify Variables")
        print("4. Show Control Variable Value")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            initialize_variables()
        elif choice == '2':
            show_variables()
        elif choice == '3':
            modify_variables()
        elif choice == '4':
            print(f"Control Variable Value: {calculate_contr()}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
