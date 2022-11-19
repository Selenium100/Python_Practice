

def wordCount(str):
    words = str.split(" ")
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

str = 'I I AM AM A A A A GOOD BOY BOY BOY'
print(wordCount(str))







