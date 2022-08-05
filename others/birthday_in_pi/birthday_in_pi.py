# This script finds your birthday in number format among the digits of pi.
# Actually, the script accepts any numerical string.
# So you can probably use any numerical sequence with it.

file = open('pi_1m.txt', 'r')                                                            # Open the file containing the number pi
pi_digits = file.read()                                                                  # Read the file and store the pi as a string to a variable
birthday = input("What sequence of digits would you like to find in pi? ")               # Ask the user for their number sequence
try:
    int(birthday)                                                                        # Check if the input is a numerical string
except:
    print("Please input only a sequence of digits and try again.\n")                     # Output an error message if the input is not according to the format because it failed the int() test
pos = pi_digits.find(birthday)                                                           # Find the number sequence in pi using the find() method
pos = pos + 1                                                                            # Account for python numbering and change to the ordinal numbering
if pos > 0:
    print("Your sequence was first found at digit " + str(pos) + " of pi.\n")            # If pos is not -1 then print a message of the number sequence's position in pi
else:
    print("Your sequence was not fgitound in the first million digits of pi.\n")         # If pos is -1 then print an error message saying it was not found.