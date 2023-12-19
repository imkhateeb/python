nums = input("Enter numbers: ")
list_of_nums = [int(n) for n in nums.split()]
print([n*n for n in list_of_nums])