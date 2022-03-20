def av_imdb(mov_list):
    mov_list = list(mov_list)
    sum = 0
    for c in mov_list:
        sum += c["imdb"]
    return sum / len(mov_list)