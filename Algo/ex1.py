def count_connections(list1: list, list2: list) -> int:
    count = 0
    my_dict = {}
    for j in list2:
        if j not in my_dict:
            my_dict[j] = 1
        else:
            my_dict[j] += 1

    for i in list1:
        if i not in my_dict:
            continue
        count += my_dict[i]

    return count
