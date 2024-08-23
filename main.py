def main():
    book_path = "books/frankenstein.txt"
    text = book_text_get(book_path)
    count = word_count(text)
    print(f"there are {count} words in this book.")
    character = character_count(text)
    

def book_text_get(path):
    with open(path) as f:
        return f.read()
    
def word_count(book):
    """
    Takes a document as a string as input and outputs the word count as an integer.
    """
    #Splits text from book into a list
    book_word = book.split()
    #Counts the length of the list to return the word count
    book_word_count = len(book_word)
    return book_word_count

def character_count(book):
    """
    Takes a document as a string as an input and outputs a dictionary with the character count of every letter that appears as a lowercase.
    """
    characters = {}
    #Lowercases the document
    lowercase_book = book.lower()
    #For loop that looks at every character in the document and keeps count of how many it has gone through
    for character in lowercase_book:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    return(characters)


main()