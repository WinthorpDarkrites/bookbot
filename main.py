def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counted_words = count(file_contents)
        counter_letters_dictionary = letters(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{counted_words} words found in the document")
        print(" ")
        for result in counter_letters_dictionary:
            print(f"The '{result[0]}' chacharacter was found {result[1]} times")
        print("--- End report ---")


def count(str):
    words = str.split()
    
    return len(words)

def letters(str):
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lower_str = str.lower()
    alphabet_dictionary = {}

    for letter in alphabet_list:
        str_len = len(lower_str)
        for i in range(0,str_len):
            if lower_str[i] == letter:
                if letter in alphabet_dictionary:
                    alphabet_dictionary[letter] += 1
                else:
                    alphabet_dictionary[letter] = 1

    sorted_result = sorted(alphabet_dictionary.items(), key=lambda item: item[1], reverse=True)

    return sorted_result


main()