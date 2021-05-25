def filter_odd_or_even(numbers, odd):
    for i in range(10):
        if (numbers[i] % 2) == 0:
            even_numbers += numbers[i]
    print(even_numbers)

def main():
    list1 = ['1', '9', '4', '12', '17', '23', '45', '2', '9', '65', '19', '55', '12', '86', '36', '28', '52', '16']
    filter_odd_or_even(list1, True)

main()