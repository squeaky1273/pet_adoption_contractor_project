# test.py

from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

class PlaylistsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""
        
        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    
    def test_index(self):
        """Test the adoptions homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Adoption', result.data)



if __name__ == '__main__':
    unittest_main()
