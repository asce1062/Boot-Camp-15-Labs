def words(word):
    my_dict = {}
    for word in word.split():
        if word.isdigit():
            word = int(word)
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict
