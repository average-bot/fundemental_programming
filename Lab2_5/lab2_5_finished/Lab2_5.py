# Imports the system-specific parameters and functions library
import sys


# Reads the file and saves the numbers in the file into a list,
# returns it to the main function
def read_file(filename):
    try:
        # Opens the file for reading
        with open(filename, 'r') as numberfile:
            number_list = []
            for line in numberfile:
                number_list += line.split()

        # Converts all the values in the list into integers
            for i in range(len(number_list)):
                number_list[i] = int(number_list[i])
            return number_list

    # If the user inputs a file name that does not excist in the folder
    except FileNotFoundError:
        print('Bad file name')


# Filters out the odd respectively even numbers from the list,
# returns the filtered list to the main function
def filter_odd_or_even(numbers, odd):
    if odd:  # Filters out the odd numbers
        odd_numbers = []
        for i in range(len(numbers)):
            if(numbers[i] % 2) != 0:
                odd_numbers.append(numbers[i])
        return odd_numbers

    elif odd is False:  # Filters out the even numbers
        even_numbers = []
        for i in range(len(numbers)):
            if(numbers[i] % 2) == 0:
                even_numbers.append(numbers[i])
        return even_numbers


# Sorts the list of numbers in a decreasing order,
# returns the sorted list into the main function
def reversed_bubble_sort(numbers):
    for i in range(len(numbers)):
        for a in range(i+1, len(numbers)):
            if numbers[i] < numbers[a]:
                numbers[i], numbers[a] = numbers[a], numbers[i]
    return numbers


# The main function fetches the input from the command line,
# calls all the other necessary functions,
# appends the lists from even and odd numbers into a list
# then prints the list with the final result on the screen
def main():
    file1 = read_file(sys.argv[1])
    file2 = read_file(sys.argv[2])
    odd_numbers = filter_odd_or_even(file1, True)
    even_numbers = filter_odd_or_even(file2, False)
    numbers = even_numbers + odd_numbers
    sorted_numbers = reversed_bubble_sort(numbers)
    print(sorted_numbers)


# Executes only if the file was run directly (not imported)
if __name__ == "__main__":
    main()
