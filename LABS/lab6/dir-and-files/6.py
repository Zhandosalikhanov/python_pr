import os

def create_files():
    x = 65
    while x != 91:
        dir_name = r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab6\dir-and-files\files_from_A_to_Z"
        file_name = chr(x) + ".txt"
        path = os.path.join(dir_name, file_name)
        f = open(path, "x")
        f.close()
        x += 1

if __name__ == '__main__':
    create_files()