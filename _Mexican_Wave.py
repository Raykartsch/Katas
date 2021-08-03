def wave(word):
    waving = [word[:i] + word[i].upper() + word[i+1:] for i in range(len(word)) if word[i].isalpha()]
    return waving
wave('hello world')