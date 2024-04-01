def delete_duplicate_words(file_path):
    with open(file_path,"r") as archive:
        text = archive.read().strip().split()
        unique_words = set(text)
        print("unique words: ",unique_words)

delete_duplicate_words("text.txt")