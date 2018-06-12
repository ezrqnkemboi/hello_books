"""
The file contains tests for books (Adding books, editing, deleting, borrowing and getting
"""
import json

from tests.BaseTests import HelloBooksTestCase


class BooksTestCase(HelloBooksTestCase):
    """This class contains all tests for users"""

    def test_admin_add_book(self):
        """Add book by admin that already exist"""
        add_book = self.add_book()
        self.assertEqual(add_book.status_code, 201)
        add_book_again = self.add_book()
        self.assertEqual(add_book_again.status_code, 200)

    def test_user_add_book(self):
        """Tests that user cannot make crud operations. Only admin do."""
        user_login = self.login_user()
        user_login_msg = json.loads(user_login.data)
        access_token = user_login_msg['access_token']
        user_add_book = self.client.post('/api/v1/books', data=json.dumps(self.add_book_data),
                                         headers={"Authorization": "Bearer {}".format(access_token)},
                                         content_type='application/json')
        self.assertEqual(user_add_book.status_code, 403)

    def test_get_all_books(self):
        """Test user can get all books"""
        self.add_book()
        get_all_books = self.client.get('/api/v1/books')
        self.assertEqual(get_all_books.status_code, 200)

    def test_get_all_books_no_books(self):
        """Tests get books when no books available"""
        get_all_books = self.client.get('/api/v1/books')
        self.assertEqual(get_all_books.status_code, 404)

    def test_get_single_book(self):
        """Test that a user can get a single book"""
        add_book = self.add_book()
        book_data = json.loads(add_book.data)
        result = self.client.get('/api/v1/books/{}'.format(book_data['book_added']['book_id']))
        self.assertEqual(result.status_code, 200)

    def test_get_unavailable_book(self):
        """Get a book that is not available"""
        unavailable_book = self.client.get('/api/v1/books/1234')
        self.assertEqual(unavailable_book.status_code, 404)

    def test_admin_can_edit_book(self):
        """Tests that a book can be edited"""
        add_book = self.add_book()
        book_data = json.loads(add_book.data)
        login_admin = self.login_admin()
        login_msg = json.loads(login_admin.data)
        access_token = login_msg['access_token']
        edit_book = self.client.put('/api/v1/books/{}'.format(book_data['book_added']['book_id']),
                                    data=json.dumps(self.edit_book_data), content_type='application/json',
                                    headers={"Authorization": 'Bearer {}'.format(access_token)}
                                    )
        self.assertEqual(edit_book.status_code, 200)

    def test_user_can_edit_book(self):
        """Testing that user can edit a book"""
        admin_add_book = self.add_book()
        book_data = json.loads(admin_add_book.data)
        login_user = self.login_user()
        login_user_msg = json.loads(login_user.data)
        access_token = login_user_msg['access_token']
        user_edit_book = self.client.put('/api/v1/books/{}'.format(book_data['book_added']['book_id']),
                                         data=json.dumps(self.edit_book_data), content_type='application/json',
                                         headers={"Authorization": 'Bearer {}'.format(access_token)}
                                         )
        self.assertEqual(user_edit_book.status_code, 403)

    def test_admin_can_delete_book(self):
        add_book = self.add_book()
        book_data = json.loads(add_book.data)
        login_admin = self.login_admin()
        login_msg = json.loads(login_admin.data)
        access_token = login_msg['access_token']
        delete_book = self.client.delete('/api/v1/books/{}'.format(book_data['book_added']['book_id']),
                                         headers={"Authorization": 'Bearer {}'.format(access_token)})
        self.assertEqual(delete_book.status_code, 204)

    def test_user_can_delete_a_book(self):
        """Test user deleting a book"""
        admin_add_book = self.add_book()
        book_data = json.loads(admin_add_book.data)
        login_user = self.login_user()
        login_msg = json.loads(login_user.data)
        access_token = login_msg['access_token']
        user_delete_book = self.client.delete('/api/v1/books/{}'.format(book_data['book_added']['book_id']),
                                              headers={"Authorization": 'Bearer {}'.format(access_token)})
        self.assertEqual(user_delete_book.status_code, 403)

    def test_delete_unavailable_book(self):
        """Test deleting book that is not available"""
        login_admin = self.login_admin()
        login_msg = json.loads(login_admin.data)
        access_token = login_msg['access_token']
        delete_unavailable_book = self.client.delete('/api/v1/books/1234',
                                                     headers={"Authorization": 'Bearer {}'.format(access_token)})
        self.assertEqual(delete_unavailable_book.status_code, 404)


