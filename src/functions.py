# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(9))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE


def keyboard_even(x):
    if (is_even(x)):
        return "Even!"
    return "Odd"


print(keyboard_even(num))
