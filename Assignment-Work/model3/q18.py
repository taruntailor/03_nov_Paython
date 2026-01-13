def is_sublist(main_list, sub_list):
    n = len(sub_list)
    for i in range(len(main_list) - n + 1):
        if main_list[i:i+n] == sub_list:
            return True
    return False


# Example
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

print(is_sublist(main_list, sub_list))
