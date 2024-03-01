def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    chars_count = count_chars(text)
    aggregated_letters = aggregate(chars_count)
    report(aggregated_letters, number_of_words, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(string):
    lowered_case_string = string.lower()
    letter_dictionary = {}
    for letter in lowered_case_string:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1

    return letter_dictionary

def sort_on(dict):
    return dict["num"]

def aggregate(chars):
    list = []
    for key, value in chars.items():
        if key.isalpha():
            list.append({"name": key, "num": value})
    return list

def report(letters, words, file_path):
    letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {file_path} ---")
    print(f"{words} words found in the document")
    print()
    for item in letters:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End Report ---")
    
    
main()
