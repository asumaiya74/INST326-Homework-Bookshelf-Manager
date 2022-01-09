# Instructions
For this homework assignment, you will read in multiple works of literature to create an index of the words used in each work (in the form of a dictionary) and a popularity index. We will assume that each one of these works exist as text files in a folder within the same directory as your python script named data. We will also assume that your script is named bookshelf.py.

Your script should contain two classes, Book and BookShelf, and at least one function (remove_punctuation, main and parse_args) that exist outside of any class. At the end of the script should be an if __name__ == "__main__": statement. Specifications for each of these required program elements are given below. You may write additional classes, methods, and/or functions if you wish.


# remove_punctuation()

**Functionality**
- This function takes a string and returns a string containing only the lower cased alphabetical characters. If the item being passed in is not a string a TypeError should be raised.

**Parameters**
- word: the input string that contains a word. This word may contain non-alphabetical characters such as numbers or punctuation marks.

**Returns**
- A lowercase string containing only the lowercased alphabetical characters from the input string with all of the non alphabetical characters stripped away. If the string did not contain any alphabetical characters (the string is empty), the function will return None.

# Book class

**Functionality**
- This class stores the text data for a single book

**Attributes**
- words: a list of all of the individual words in the book. The elements in this list do not have to be unique.

**Methods**
- __init__()
