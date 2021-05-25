import sys

def read_file(filename):
    try:
        with open(filename, 'r') as numberfile:
            number_list = []
            for line in numberfile:
                number_list += line.split()
            
        # Converting all the values in the list into integers
            for i in range(len(number_list)):
                number_list[i] = int(number_list[i])
            return number_list
    except:
        print('Error')


def filter_odd_or_even(numbers, odd):
    if odd:
        odd_numbers = []
        for i in range(len(numbers)):
            if(numbers[i] % 2) != 0:
                odd_numbers.append(numbers[i])
        return odd_numbers

    elif odd == False:
        even_numbers = []
        for i in range(len(numbers)):
            if(numbers[i] % 2) == 0:
                even_numbers.append(numbers[i])
        return even_numbers


def reversed_bubble_sort(numbers):
    for i in range(len(numbers)):
        for a in range(i+1, len(numbers)):
            if numbers[i] < numbers[a]:
                numbers[i], numbers[a] = numbers[a], numbers[i]
    return numbers


def main():
    list1 = read_file(sys.argv[1])
    list2 = read_file(sys.argv[2])
    even_numbers = filter_odd_or_even(list1, False)
    odd_numbers = filter_odd_or_even(list2, True)
    numbers = even_numbers + odd_numbers
    sorted_numbers = reversed_bubble_sort(numbers)
    print(sorted_numbers)


main()
