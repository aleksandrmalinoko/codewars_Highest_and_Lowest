def min_max(array_of_numbers):
    max_elem = 0 - float("inf")
    min_elem = (float("inf"))
    for i in range(len(array_of_numbers)):
        temp_elem = int(array_of_numbers[i])
        if temp_elem > max_elem:
            max_elem = temp_elem
        if temp_elem < min_elem:
            min_elem = temp_elem
    return f"{str(max_elem)} {str(min_elem)}"


def high_and_low(string_of_numbers):
    array_of_number = string_of_numbers.split()
    return min_max(array_of_number)


if __name__ == '__main__':
    print(high_and_low("1 2 3 4 5"))
