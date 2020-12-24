"""
Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

- Expected Output 1:
How many fibonacci numbers would you like to generate? 5
[1, 1, 2, 3, 5]
How many fibonacci numbers would you like to generate? 10
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
How many fibonacci numbers would you like to generate? 1
[1]
"""


def fibo(num):
    arr = [1, 1]
    if num == 1:
        return arr[num]
    elif num == 2:
        return arr
    else:
        for i in range(num - 2):
            # arr.append(arr[i] + arr[i+1])
            arr.append(arr[-2] + arr[-1])
        return arr


print(fibo(10))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Input/Output
while True:
    try:
        sample = int(
            input("How many numbers do yo want from Fibonacci Array? "))
        print(fibo(sample))
        break
    except:
        print("Invalid Entry.")
