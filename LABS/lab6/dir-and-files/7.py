def copy_paste(copy_p, paste_p):
    c = open(copy_p, "r")
    p = open(paste_p, "w")
    
    for x in c.readlines():
        p.write(x)

    c.close()
    p.close()

if __name__ == '__main__':
    copy_paste(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab6\dir-and-files\copy.txt",
               r"C:\Users\User\OneDrive\Рабочий стол\python_pr\LABS\lab6\dir-and-files\paste.txt")