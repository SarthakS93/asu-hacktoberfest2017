def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        smallest_number = numbers[i]
        smallest_number_index = i
        for j in range(i + 1, n):
            if numbers[j] < smallest_number:
                smallest_number = numbers[j]
                smallest_number_index = j

        numbers[i], numbers[smallest_number_index] = numbers[smallest_number_index], numbers[i]

    return numbers
