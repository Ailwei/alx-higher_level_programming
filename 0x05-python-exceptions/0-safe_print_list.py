def safe_print_list(my_list=[], x=0):
    count = 0;
    try:
        for i in range(x):
            item = my_list[i]
            print(item, end=" ")
            count += 1
    except IndexError:
        pass
    print()
    return count

