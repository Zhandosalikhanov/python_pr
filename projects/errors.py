from math import sqrt

l = []
l1 = []
m_val = 0
st_dev = 0

def mean():
    m_val = sum(l) / len(l)

    print("The mean value:")
    print(sum(l), '/', len(l), '=', m_val, '\n')
    return m_val

def abs_er():
    print("Absolute errors:")
    for x in l:
        print(m_val, '-', x, '=', m_val - x, '\n')
        l1.append(m_val - x)

def sdem():
    st_dev = sqrt(sum(l) / (len(l) * (len(l) - 1)))

    print("The Standart Deviation Value:")
    print("sqrt(", sum(l), '/', len(l) * (len(l) - 1), ') =', st_dev, '\n')
    return st_dev

def relative():
    print("The relative error")
    print(2.8, '*', st_dev, "* 100% /", m_val, '=',
            2.8 * st_dev * 100 / m_val, '%\n')

def conf():
    print("The confidence interval:")
    print(m_val, '+-(', 2.8, '*', st_dev, ') =',
            m_val, '+-', 2.8 * st_dev, '\n')

if __name__ == '__main__':

    print("Enter values:")

    l = list(map(lambda x: float(x), input().split()))
    
    m_val = mean()

    abs_er()
    
    l = list(map(lambda x: pow(float(x), 2), l1))
    
    st_dev = sdem()
    
    relative()
    
    conf()