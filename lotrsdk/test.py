import unittest
import lotrsdk


class TestNotNone(unittest.TestCase):

    def test_get_movies_not_null(self):
        
        r = lotrsdk.get_movies()
        status = r['status']
        self.assertEqual(str(status), '200')
        self.assertIsNotNone(lotrsdk.get_movies())

    def test_get_one_movie_not_null(self):

        r = lotrsdk.get_one_movie('5cd95395de30eff6ebccde5b')
        status = r['status']
        self.assertEqual(str(status), '200')        

    def test_get_movies_quote_not_null(self):
        
        r = lotrsdk.get_quote_fom_movie('5cd95395de30eff6ebccde5b')
        status = r['status']
        self.assertEqual(str(status), '200')

unittest.main()

