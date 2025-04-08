from collections import Counter

def read_file(filename: str):
    file_content = None
    with open(filename, "r") as f:
        file_content = f.read().strip().split(" ")
    return file_content
        
def count_unique_words(file_content):
    return Counter(read_file(file_content))
