def solve(legs, heads, i):
    if (i * 4) + (heads - i) * 2 == legs:
        return("We have", i, "rabbits and", heads - i, "chickens")
    else:
        return(solve(legs, heads, i + 1))

if __name__ == "__main__":
    print(solve(94, 35, 1))