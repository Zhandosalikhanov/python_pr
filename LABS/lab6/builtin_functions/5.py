def all_true(tp):
    return all(tp)

if __name__ == '__main__':
    print(all_true((1, 2, True)))
    print(all_true((1, 2, False)))
    print(all_true((0, True, True)))
    print(all_true((1, True, True)))