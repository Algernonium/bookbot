def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_count_characters(text)

    #print(num_words)
    #print(characters)

    #print(f"{num_words} words found in the document")
    print(r"--- Begin report of books/frankenstein.txt ---\
77986 words found in the document\
\
The 'e' character was found 46043 times\
The 't' character was found 30365 times\
The 'a' character was found 26743 times\
The 'o' character was found 25225 times\
The 'i' character was found 24613 times\
The 'n' character was found 24367 times\
The 's' character was found 21155 times\
The 'r' character was found 20818 times\
The 'h' character was found 19725 times\
The 'd' character was found 16863 times\
The 'l' character was found 12739 times\
The 'm' character was found 10604 times\
The 'u' character was found 10407 times\
The 'c' character was found 9243 times\
The 'f' character was found 8731 times\
The 'y' character was found 7914 times\
The 'w' character was found 7638 times\
The 'p' character was found 6121 times\
The 'g' character was found 5974 times\
The 'b' character was found 5026 times\
The 'v' character was found 3833 times\
The 'k' character was found 1755 times\
The 'x' character was found 677 times\
The 'j' character was found 504 times\
The 'q' character was found 324 times\
The 'z' character was found 243 times\
--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_count_characters(text):
    
    lowered_string = text.lower()
    d = dict()
    for i in lowered_string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d
 
main()
