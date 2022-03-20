def Converter(gram):
    return gram / 28.3495231

if __name__ == "__main__":
    gram = float(input("Enter gramms: "))
    print(gram, "gramms in ounces are:", Converter(gram))