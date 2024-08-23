def main():
    book_path = "books/frankenstein.txt"
    text = book_text_get(book_path)
    count = word_count(text)
    character = character_count(text)
    sorted_character = character_sort(character)
    book_report(book_path, count, sorted_character)
    
    

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
    characters_dict = {}
    #Lowercases the document
    lowercase_book = book.lower()
    #For loop that looks at every character in the document and keeps count of how many it has gone through
    for character in lowercase_book:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    
    return characters_dict

def sort_key(dict):
    """
    Takes a dictionary as input and returns the second item in the key.
    """
    for key in dict:
        num = dict[key]
        return num

def character_sort(dict):
    """
    Takes a dictionary with the character count as input.
    Removes any non-letter character from the dictionary and appends them to a new list.
    Returns a sorted list of the character count in descending order.
    """
    sorted_list = []
    #Converts dictionary to a list, taking out any non-letter keys
    for key in dict:
        num = dict[key]
        if key.isalpha() == True:
            sorted_list.append({key:num})
        else:
            pass

    sorted_list.sort(reverse=True, key=sort_key)

    return sorted_list

def book_report(book_path, word_count, character_count):
    """
    Takes the book path, word count, and character count as input
    Outputs a book report with the input information
    """
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for key in character_count:
        for char in key:
            num = key[char]
            print(f"The {char} character was found {num} times")

    print("--- End report ---")
    return None


main()