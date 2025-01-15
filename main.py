def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        count(file_contents)

def count(str):
    words = str.split()
    print(len(words))

def letters(str):
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lower_str = str.lower()


main()