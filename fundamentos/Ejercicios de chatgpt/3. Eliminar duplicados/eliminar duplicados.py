with open("text.txt","r") as archive:
    text = archive.read().split()
    print(text)
    unique_words = set(text)
    print("unique words: ",unique_words)