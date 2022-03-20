from movies import movies

def av_imdb_of_categ(categ):
    sum = 0
    n = 0
    for c in movies:
        if c["category"] == categ:
            sum += c["imdb"]
            n += 1
    return sum / n