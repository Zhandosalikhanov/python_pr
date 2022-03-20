import os

def del_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        raise Exception("The given path does not exist")

if __name__ == '__main__':
    del_file(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab6\dir-and-files\trash")
    del_file(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab6\dir-and-files\box")