# Reading Books


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_freq(text):
    text = text.lower()
    freqs = {}
    for i in text:
        if i in freqs and i.isalpha():
            freqs[i] += 1
        elif i.isalpha():
            freqs[i] = 1
    return freqs


def list_of_dicts(dict):
    grand_list_of_dicts = []
    for i in dict:
        grand_list_of_dicts.append({"char": i, "freq": dict[i]})
    return grand_list_of_dicts


def sort_dict(dict):
    return dict["freq"]


def report(words: int, list_dict: list[dict]):
    print("---------Begin Report---------")
    print(f"{words} words found in the document\n")

    for i in list_dict:
        num1 = i["char"]
        num2 = i["freq"]
        print(f"The {num1} character was found {num2}")

    print("----------End Report----------")


def main():
    book_path = "./books/frankenstein.txt"
    text = get_text(book_path)
    words = text.split()
    print(len(words))
    freqs = get_freq(text)
    dict_of_chars = list_of_dicts(freqs)
    dict_of_chars.sort(reverse=True, key=sort_dict)
    print(dict_of_chars)
    report(len(words), dict_of_chars)


main()
