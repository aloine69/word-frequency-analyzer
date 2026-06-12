def start_analyzer():
    word_count = {}
    count_words(word_count)
    prev = 0
    for key, value in word_count.items():
        if value > prev:
            print(f"Top most common word is {key} with a count of {value}")
            prev = value


def count_words(dict):
    words = read_from_file("data.txt")
    word_list = words.split(" ")
    for word in word_list:
        count = word_list.count(word)
        dict[word] = count


def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read().replace("\n", " ")
            return data
    except FileNotFoundError:
        print("File not found!")


start_analyzer()
