import unittest
import App


class TestApp(unittest.TestCase):

    def test_read_input_correctly_from_file(self):
        parsed_input = {
            "lon": 3.879483,
            "lat": 43.608177,
            "n": 3,
            1: "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217",
            2: "2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849",
            3: "3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854"
        }
        self.assertEqual(App.load("./resources/input.txt"), parsed_input, "Should load file into dict")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
