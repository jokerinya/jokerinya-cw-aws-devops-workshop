def calculate(mylist):
    max_diff = 0
    for i in range(len(mylist)):
        for j in mylist[i:]:
            temp_diff = j - mylist[i]
            if temp_diff > max_diff:
                max_diff = temp_diff
    return max_diff

list_a = [75,73,60,100,120,130]  # Output must be 70
list_b = [10,20,23,22,17,30]  # Output must be 20
list_c = [1,6,19,59,30,60]  # Output must be 59
list_d = [9, 11, 8, 5, 7, 10]  # Output must be 5

print(f"List a profit=> {calculate(list_a)}")
print(f"List b profit=> {calculate(list_b)}")
print(f"List c profit=> {calculate(list_c)}")
print(f"List d profit=> {calculate(list_d)}")