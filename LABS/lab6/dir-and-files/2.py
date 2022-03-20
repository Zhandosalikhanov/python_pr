import os

def test_file(path):
    f = open(path, "r")

    if os.path.exists(path):
        print("File exists..")
    else:
        print("File do not exists..")
        
    if f.readable():
        print("File is readable..")
    else:
        print("File is not readable..")

    f = open(path, "a")

    if f.writable():
        print("File is writable..")
    else:
        print("File is not writable..")
        
    if  os.access(path, os.X_OK):
        print("File is executable..")
    else:
        print("File is not executable..")
    
    f.close()

if __name__ == '__main__':
    test_file(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\3.py")