from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_suit_id = ObjectId('5d55cffc4a3d4031f42827a3')

sample_suit =
    {
        "Name":"Jumpman",
        "Price":"2000000",
        "IMG URL":"anti-gravity kit, flexible materials"
    }

sample_form_data = {
        "name":sample_suit['name'],
        "price":sample_suit['price'],
        "img_url":sample_suit['img_url']
    }


class ContractorTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""
        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the suits homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Suits Homepage', result.data)

    def test_new(self):
        """Test the new playlist creation page."""
        result = self.client.get('/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Suit', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_suit(self, mock_find):
        """Test showing a single suit."""
        mock_find.return_value = sample_suit

        result = self.client.get(f'/suit/{sample_suit_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Jumpman', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_suit(self, mock_find):
        """Test showing a single suit."""
        mock_find.return_value = sample_suit

        result = self.client.get(f'/suits/edit/{sample_suit_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Jumpman', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_delete_game(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/delete/{sample_game_id}', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_game_id})


    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_playlist(self, mock_insert):
        """Test submitting a new suit."""
        result = self.client.post('/suits', data=sample_form_data)

        # After submitting, should redirect to that playlist's page
        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_suit)


if __name__ == '__main__':
    unittest_main()
