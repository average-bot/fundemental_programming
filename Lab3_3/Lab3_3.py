import pickle


# Displays the menu on the screen
def display_menu():
    print('1. Add file')
    print('2. Calculate')


# Cross references the numbers from the text files,
# returns the number that is in all the files
def cross_reference(files):
    num_list = []
    suspect_num = set()

    for number_file in files:
        with open(number_file, 'r') as numfile:
            for line in numfile:
                line = line.rstrip('\n')
                num_list.append(line)

    for i in set(num_list):
        if len(files) == num_list.count(i):
            suspect_num.add(i)

    return suspect_num


# Connects the number to the name of the person
def map_numbers_to_names(numbers, filename):
    suspects = []
    with open(filename, 'rb') as ownersfile:
        owners = pickle.load(ownersfile)
        for number in numbers:
            if number in owners:
                suspect = owners.get(number)
                suspects.append(suspect)
            else:
                suspects.append('Unknown (' + number + ')')
    return suspects


# Displays the names of thee suspects on the screen
def display_suspects(names):
    print('The following persons was present on all crime scenes:')
    print('------------------------------------------------------')
    if len(names) > 0:
        for name in names:
            print(name)
    else:
        print('No matches')


def main():
    filenames = []
    ownersfile = 'C:/Users/Sandr/Downloads/python/Lab3_3/Lab3_3_owners.bin'

    choice = 0
    while choice != 2:
        display_menu()
        choice = int(input('Enter choice: '))
        if choice == 1:
            filenames.append(input('Enter a filenameinclude full path: '))

    try:
        num_set = cross_reference(filenames)
        suspects = map_numbers_to_names(num_set, ownersfile)
        display_suspects(suspects)

    except FileNotFoundError:
        print('Error: There was a problem with at least one of the files.')


# Executes only if the file was run directly (not imported)
if __name__ == "__main__":
    main()
