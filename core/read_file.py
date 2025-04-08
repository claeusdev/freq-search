from collections import Counter

def read_file(filename: str):
    file_content = []
    with open(filename, "r") as f:
        sentences = f.read().strip().split(".")
        for sentence in sentences:
            words_in_sentence = sentence.strip("").split(" ")
            single_sentence = " ".join(words_in_sentence)
            file_content.append(single_sentence.strip())  
    content = []
    for s in file_content:
        words = s.split()
        content.append(" ".join(s.split(" ")))
    print(" ".join(content))

    return " ".join(content).split(" ")
        
def count_unique_words(file_content):
    return Counter(read_file(file_content))
