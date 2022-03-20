import movies

def categ_filt(catg):
    catg_sub_l = []
    for c in movies.movies:
        if c["category"] == catg:
            catg_sub_l.append(c["name"])
    return catg_sub_l

print(categ_filt("Thriller"))