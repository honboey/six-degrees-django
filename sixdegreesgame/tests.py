from django.test import TestCase

from .views import initialise_rappers

# Create your tests here.


class IndexViewsTests(TestCase):
    def test_initialise_rappers(self):
        """
        Test that we get two rappers from the list and a URL for their image on Spotify
        """
        rappers = initialise_rappers()

        # Check that it's a tuple with two dictionaries
        self.assertIsInstance(rappers, tuple)
        self.assertEqual(len(rappers), 2)
        self.assertIsInstance(rappers[0], dict)
        self.assertIsInstance(rappers[1], dict)

        # Test specific keys or values in the dictionaries
        self.assertIn("name", rappers[0])
        self.assertIsInstance(rappers[0]["name"], str)
        self.assertIn("https:", rappers[0]["image"]["url"])
        self.assertIn("name", rappers[1])
        self.assertIsInstance(rappers[1]["name"], str)
        self.assertIn("https:", rappers[1]["image"]["url"])
