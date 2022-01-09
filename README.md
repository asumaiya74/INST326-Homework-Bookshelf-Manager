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
  - Parameters
    - Self
    - Path - The path to the file that we are going to read.
  - Functionality
    - The init method should open the file specified by the path for reading and set the words to attribute to a list containing all of the words in the file split on the spaces. You should also use the remove_punctuations() function within a list comprehension to remove all of the non-alphabetical characters from each element in the list and set the resulting list to the words attribute. While you are at it, you should also remove any elements of the list that were determined to be None by remove_punctuations(). The resulting words attribute should be a list of string elements where each element contains only lowercase alphabetical characters.
    
- unique_words()
  - Parameters
    - Self  
  - Functionality
    - This method should return a set created from the words attribute (which should be a list).


# BookShelf class

**Functionality**
- This class stores the index for words in books as they are provided.
**Attributes**
- index: a dictionary representing an index of the words of a book where the keys are the unique words found in a series of books, and the values are lists containing string elements that represent the name of the book in which that word is found.
- popularity_index: a dictionary based on the index attribute which is itself an index where the keys are integers that represent how many books a word is found in and the values are the words that correspond to this count. For example: if the words "tree" and "car" are found in two different books, and the word "lantern" is found in one book the dictionary might look like so: {2:["tree", car], 1:["lantern"]}.

  > NOTE: This attribute will start off empty and will not be created until find_popularity() is invoked later.

**Methods**

















