from math import sqrt

class Data:
    def __init__(self, list: list):
        self.list = list
        self.size = len(list)
        self.errors = []
        
    def mean(self):
        self.sum = sum(self.list)
        self.m_val = self.sum / self.size

        print("The mean value:")
        print(f'{self.sum} / {self.size} = {self.m_val} \n')
        
    def abs_er(self):
        print("Absolute errors:")
        
        for x in self.list:
            error = self.m_val - x
            self.errors.append(pow(self.m_val - x, 2))
            
            print(f'{self.m_val} - {x} = {error} \n')

    def SDEM(self):
        self.rel_sum = sum(self.errors)
        self.sdem = sqrt(self.rel_sum / (self.size * (self.size - 1)))

        print("The Standart Deviation Value:")
        print(f'sqrt({self.rel_sum} / ({self.size} * ({self.size} - 1))) = {self.sdem} \n')
        
    def relative(self):
        self.rel_er = 2.8 * self.sdem * 100 / self.m_val
        
        print("The relative error:")
        print(f'2.8 * {self.sdem} * 100% / {self.m_val} = {self.rel_er}% \n')
        
    def conf_int(self):
        self.conf = f'{self.m_val} +- {2.8 * self.sdem}'
        
        print("The confidence interval:")
        print(f'{self.m_val} +- 2.8 * {self.sdem} = {self.conf} \n')
        
if __name__ == '__main__':
    print('Enter values: ', end='')
    
    l = input().split()
    l = list(map(lambda x: float(x), l))
    
    d = Data(l)
    
    d.mean(), d.abs_er(), d.SDEM(), d.relative(), d.conf_int()