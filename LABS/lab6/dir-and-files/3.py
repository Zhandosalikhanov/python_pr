from pathlib import Path

def par_dir(p):
    p = Path(p)

    if p.exists():
        return str(p.parent)
    else:
        return "Path do not exists.."

if __name__ == '__main__':
    print(par_dir(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\3.py"))