def n_up_low_chr(s):
    upper = sum(map(str.isupper, s))
    lower = sum(map(str.islower, s))
    return (upper, lower)

if __name__ == '__main__':
    print(n_up_low_chr("Zhandos_Alikhanov_2004"))