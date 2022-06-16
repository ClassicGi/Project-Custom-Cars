# Prints a line of equal signs
print("===================")

# Display title
print("Welcome to the UMBC")
print("Car Customization Form")

# Prints a line of equal signs
print("===================")

# Prints a blank line
print()

# Prints description
print("(For multiple choice problems, please enter the letter of the selection you're looking for")

# Display header
print("~ Make & Model ~")

# Display question 1 with multiple choice
print("1. What Body Styles of Car are you ordering?")

# Display option 1
print("  a. Sedan")

# Display option 2
print("  b. Hatchback")

# Display option 3
print("  c. SUV")

# Display option 4
print("  d. Pickup")

# Enter the option a - d
modelOption = input("Pleas enter 'a' - 'd': ")

# Print a blank license
print()

# Display question 2 with yes or no question
print("2. Would you like to upgrade to the hatchback version")

# Enter answer
versionOption = input("Please enter 'yes' or 'no': ")

# Print a blank license
print()

# Display header
print("~ Exterior ~")

# Display question 3 short response question
print("3. What type of spare wheel would you like?")

# Enter short response answer
spareOption = input("You may enter the type of spare wheel you'd like: ")

# Print a blank license
print()

# Display question 4 with yes or no question
print("4. Would you like a sunroof?")

# Enter answer
sunroofOption = input("Please enter 'yes' or 'no': ")

# Print a blank license
print()

# Display header
print("~ Interior ~")

# Display question 5 with multiple choice
print("5. Select one of the following car stereos ")

# Display option 1
print("  a. Apple CarPlay compatible car stereos")

# Display option 2
print("  b. Android Auto compatible car stereos")

# Display option 3
print("  c. Bluetooth car stereos")

# Enter the option a - c
stereosOption = input("Pleas enter 'a' - 'c': ")

# Print a blank license
print()

# Display question 6 short response question
print("3. Please enter what color you'd like the interior to be ")

# Enter short response answer
colorOption = input("You may enter the color of interior you'd like: ")

# Print a blank license
print()

# Prints a line of equal signs
print("===================")

# Print a blank license
print()

# Display header
print("~ Summary ~")

# Display summary
print(f'modelOption: {modelOption}')
print(f'versionOption: {versionOption}')
print(f'spareOption: {spareOption}')
print(f'sunroofOption: {sunroofOption}')
print(f'stereosOption: {stereosOption}')
print(f'colorOption: {colorOption}')