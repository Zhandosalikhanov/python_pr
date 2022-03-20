f = int(input("Enter fahrenheit: "))
cel = lambda x: (5/9) * (x - 32)

if __name__ == "__main__":
    print(f, "fahrenheit in celcius:", cel(f), 'C')