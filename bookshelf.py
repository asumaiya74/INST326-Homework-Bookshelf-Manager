"""Create and manage bookshelf data."""
from argparse import ArgumentParser
from pathlib import Path
import sys
import re


def remove_punctuation(word):
    """
    Takes a string and returns a string containing only the lower cased alphabetical
    characters
        Args: 
        word(str): The input string that contains a word but may contain non-alphabetical characters 
        such as numbers or punctuation marks

        Raises:
        TypeError - if item being passed in is not a String

        Returns:
        A lowercase string containing only the lowercased alphabetical characters from the input string 
        with all of the non alphabetical characters stripped away. Return None
    """


    if isinstance (word, str):
        lower_alphabetical_characters = word.lower()
        remove_number  = ''.join([i for i in lower_alphabetical_characters if i.isalpha()])
        if remove_number != "":
            return remove_number
        else:
            return None
    else: 
        raise TypeError("That was not a string")



class Book(): 
    """
    This class stores the text data for a single book
        Attributes: 
            words: a list of all of the individual words in the book. The elements in this list 
            do not have to be unique.
            
            ___init___: The init method should open the file specified by the path for reading 
            and set the words to attribute to a list containing all of the words in the file split 
            on the spaces
        
        Returns the unique words within the book
        Returns: 
            A set created from the words attribute(which should be a list).
    """


    def __init__(self, path):
        file_context = open(path, "r", encoding="utf-8").read().split()
        self.words = [remove_punctuation(text) for text in file_context if remove_punctuation(text) != None]
    
        
    def unique_words(self):
        return set(self.words)


class BookShelf():
    """ 
    This class stores the index for words in books as they are provided

    Attributes:
        index: a dictionary representing an index of words in a book
        (keys are the unique words, values are lists containing of 
        the names of book where the word is found)

        popularity_index: a dictionary based on the 'index' attribute itself
        (keys are the number of books a word is found in, values are words that correspond to that count)
    
    Creates a book object from the text name passed in
    Args:
        word: a list containing names of books that use that word
        text(str): This will create a book object from the text name that is being passed in.
    """

    def __init__(self):
        self.index = {}
        self.popularity_index = {}

  
    def add_books(self, text):
        book_one = Book(text)
        words = list(book_one.unique_words())
        book_name = text
        for word in words:
            if word in self.index:
                if book_name not in self.index[word]:
                    self.index[word].append(book_name)
            else: 
                self.index[word] = [book_name]

    def find_popularity(self):
        self.popularity_index.clear()
        for word,book in self.index.items():
            count = len(book)
            if count in self.popularity_index:
                if word not in self.popularity_index[count]:
                    self.popularity_index[count].append(word)
            else: 
                self.popularity_index[count] = [word]

                

def main(Library):
    """ 
    Create an instance of bookshelf. Use each path in the library list 
    (the list that ispassed in) to invoke the add_books method on that bookshelf instance
    and find_popularity() method of the instance of bookshelf that was created.

    Args:
        library(str): A list of strings where the strings are paths to text 
        files which are books on your machine

    Returns:
        The index attribute, length of index, and popularity_index of bookshelf
        as tuple
    """
    
    book_shelf = BookShelf()
    for book_one in Library:
        book_shelf.add_books(book_one)
    book_shelf.find_popularity()
    print(len(book_shelf.index))
    return (book_shelf.index, len(book_shelf.index), book_shelf.popularity_index)

def parse_args(args_list):
    """This function will create an instance of an ArgumentParser 
    object and assign one argument to it named books 

    Args:
        books (str): Accepts any number of command line arguments (but at least one) 
        and create a list of these arguments
        args_list (list) : A list of command line arguments.

    Returns:
        The created ArgumentParser object
    """
    parser = ArgumentParser()

    parser.add_argument('books', type=str, nargs='+')
    return parser.parse_args(args_list)


if __name__ == "__main__":
    """
    Create a list of strings which are the paths to the text files that will be indexing
    """
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.books)