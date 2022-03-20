def wrt_list(path, list):
    f = open(path, "a")
    f.write(str(list))
    f.close()

if __name__ == '__main__':
    l = ["ape", "banana", 1, 2]
    wrt_list(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\1.py", l)