"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


numbers.sort()
print(numbers)



if len(numbers) % 2 == 0:
    median_index = (int(len(numbers)/2)) - 1
    median = (numbers[median_index] + (numbers[median_index + 1])) / 2
else:
    median_index = int((len(numbers) + 1) /2) - 1
    median = numbers[median_index]

print(median)


