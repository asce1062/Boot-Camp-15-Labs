def find_max_min(numbers):
    num_list = []
    minimum = min(numbers)
    maximum = max(numbers)
    if maximum == minimum:
        num_list.append(len(numbers))
    else:
        num_list.append(minimum)
        num_list.append(maximum)
    return num_list
