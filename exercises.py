number_list = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number : "))
    number_list.append(num)

print("The list of numbers is:", number_list)
