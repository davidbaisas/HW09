import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover = BookLover('David', 'David@virginia.edu', 'Non-Fiction')
        booklover.add_book('Harry Potter', 4)
        book_actual = booklover.book_list['book_name'][0]
        book_expected = 'Harry Potter'
        self.assertEqual(book_actual, book_expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover = BookLover('David', 'David@virginia.edu', 'Non-Fiction')
        booklover.add_book('Alice in Wonderland', 4)
        with self.assertRaises(ValueError) as exception_context:
            booklover.add_book('Alice in Wonderland', 4)
        self.assertEqual(str(exception_context.exception), 'Book already in book list. Cannot add duplicate book!')
            
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover = BookLover('David', 'David@virginia.edu', 'Non-Fiction')
        booklover.add_book('Chronicles of Narnia', 4)
        self.assertTrue(booklover.has_read('Chronicles of Narnia'), 'Book test value not true.')
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover = BookLover('David', 'David@virginia.edu', 'Non-Fiction')
        booklover.add_book('Dr. Seuss', 4)
        self.assertFalse(booklover.has_read('Chronicles of Narnia'), 'Book test value not false.')
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover = BookLover('David', 'David@virginia.edu', 'Non-Fiction')
        booklover.add_book('Alice in Wonderland', 4)
        booklover.add_book('Chronicles of Narnia', 4)
        booklover.add_book('Dr. Seuss', 4)
        self.assertEqual(booklover.num_books_read(), 3, 'Number of books does not match test.')

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover = BookLover('David', 'David@virginia.edu', 'Non-Fiction')
        booklover.add_book('Alice in Wonderland', 3)
        booklover.add_book('Chronicles of Narnia', 5)
        booklover.add_book('Dr. Seuss', 3)
        self.assertEqual(booklover.fav_books()['book_rating'].values[0], 5, 'Book Rating values do not match.')
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)