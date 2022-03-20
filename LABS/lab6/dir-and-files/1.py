from os import listdir

def files_in(path):
    return listdir(path)

if __name__ == '__main__':
    print(files_in(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab1"))
    print(files_in(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab2"))
    print(files_in(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab4"))
    print(files_in(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab4"))
    print(files_in(r"C:\Users\User\OneDrive\Рабочий стол\python_pr"))
