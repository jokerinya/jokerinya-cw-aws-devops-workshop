print("###  This program finds the largest number in the 5 (five) numbers given by user ###")

num_list = []

for i in range(5):
    while True:
        num = input(f"Please enter the {i + 1}. number: ")
        if (num.isdecimal()):
            num = int(num)
            num_list.append(num)
            break
        else:
            print("Not Valid Input !!!")


max_el = num_list[0]
for i in num_list:
    if max_el < i: max_el = i

print(f"Max number is {max_el}")
