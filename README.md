# Instructions
For this homework assignment, you will read in multiple works of literature to create an index of the words used in each work (in the form of a dictionary) and a popularity index. We will assume that each one of these works exist as text files in a folder within the same directory as your python script named data. We will also assume that your script is named bookshelf.py.

Your script should contain two classes, Book and BookShelf, and at least one function (remove_punctuation, main and parse_args) that exist outside of any class. At the end of the script should be an if __name__ == "__main__": statement. Specifications for each of these required program elements are given below. You may write additional classes, methods, and/or functions if you wish.


# remove_punctuation()
**Functionality**
- This class stores the index for words in books as they are provided.

**Attributes**
- **index**: a dictionary representing an index of the words of a book where the keys are the unique words found in a series of books, and the values are lists containing string elements that represent the name of the book in which that word is found.
- **popularity_index**: a dictionary based on the index attribute which is itself an index where the keys are integers that represent how many books a word is found in and the values are the words that correspond to this count. For example: if the words "tree" and "car" are found in two different books, and the word "lantern" is found in one book the dictionary might look like so: {2:["tree", car], 1:["lantern"]}.

> Note: This attribute will start off empty and will not be created until find_popularity() is invoked later.


# __init__()

# add_books()
# find_popularity()

> Note: This attribute will start off empty and will not be created until find_popularity() is invoked later.


**Attributes**
