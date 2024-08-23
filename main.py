def main():
    book_path = "books/frankenstein.txt"
    text = book_text_get(book_path)
    count = word_count(text)
    print(f"there are {count} words in this book.")
    

def book_text_get(path):
    with open(path) as f:
        return f.read()
    
def word_count(book):
    #Splits text from book into a list
    book_word = book.split()
    #Counts the length of the list to return the word count
    book_word_count = len(book_word)
    return book_word_count

main()