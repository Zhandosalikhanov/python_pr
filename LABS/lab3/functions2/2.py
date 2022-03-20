from re import sub
import movies

def IMBD_high_list():
    imbd_sub_l = []
    for c in movies.movies:
        if c["imdb"] > 5.5:
            imbd_sub_l.append(c["name"])
    return imbd_sub_l