def mean(numbers):
    mean_value = 0
    for num in numbers:
        mean_value += num
    mean_value /= len(numbers)
    return mean_value
