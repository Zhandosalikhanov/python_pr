def del_dupl(my_list):
    my_list = list(my_list)
    for c in my_list:
        while my_list.count(c) != 1:
            i = my_list.index(c)
            my_list.pop(i)
    return my_list

if __name__ == "__main__":
    l = [1, 2, 1, 5, 6, 5, 5, 1]
    print("Before deleting duplicates:")
    print(l)
    print("After deleting duplicates:")
    print(del_dupl(l))