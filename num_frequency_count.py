def num_frequency_count(numbers):
    frequency = {}
    for n in numbers:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
    return frequency

print(num_frequency_count([2, 4, 6, 2, 324, 2, 7, 6, 3, 43, 45, 43, 2, 6, 7, 8, 3, 4576, 34]))