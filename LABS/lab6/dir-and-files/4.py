def n_lines(p):
    f = open(p, "r")
    ans = len(f.readlines())
    f.close()
    return ans

if __name__ == '__main__':
    print(n_lines(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\1.py"))