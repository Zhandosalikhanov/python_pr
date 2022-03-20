import movies

def isIMDB_high(name):
    for c in movies.movies:
        if c["name"] == name and c["imdb"] > 5.5:
            return True
        elif c["name"] == name and c["imdb"] <= 5.5:
            return False