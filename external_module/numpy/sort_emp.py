# Example lists
employee_names = ['Alice', 'Bob', 'Charlie']
employee_salaries = [70000, 80000, 65000]
employee_ids = [123, 456, 789]

# Zipping the lists into a list of tuples
employees = list(zip(employee_names, employee_salaries, employee_ids))
print(employees)

# Custom bubble sort function to sort by salary
def bubble_sort_custom(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sorting the list of tuples by salary using the custom bubble sort
bubble_sort_custom(employees)

print(employees)
