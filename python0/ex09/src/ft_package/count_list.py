def count_in_list(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count
