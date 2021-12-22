# book-titles

This is a special book categorization program, 
which assigns each book a special code based on its title.

The code is equal to the first letter of the book, 
followed by the number of characters in the tile.

For example, for the book "Harry Potter", 
the code would be: H12,
as it contains 12 characters (including space).

There is a books.txt file, which inludes the book titles,
each one written on a separate line.

The program will read the title one by one and output the code 
for each book on a separate line. 

For example, if the books.txt file contains:
Some book
Another book

The program should output:
S9
A12

We will be using readlines() method on the script. 
