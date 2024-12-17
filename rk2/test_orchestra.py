# test_orchestra_module.py

import unittest
from orchestra_module import (
    Orchestra, 
    Musician, 
    MusicianOrchestra, 
    OrchestraManager
)


class TestOrchestraManager(unittest.TestCase):
    def setUp(self):
        self.orchestras = [
            Orchestra(1, 'Симфонический Оркестр'),
            Orchestra(2, 'Камерный Оркестр'),
            Orchestra(3, 'Джазовый Оркестр')
        ]

        self.musicians = [
            Musician(1, 'Александров', 5, 1),
            Musician(2, 'Иванов', 3, 2),
            Musician(3, 'Антонов', 7, 1),
            Musician(4, 'Борисов', 2, 3),
            Musician(5, 'Андреев', 4, 3)
        ]

        self.musician_orchestra_links = [
            MusicianOrchestra(1, 1),
            MusicianOrchestra(2, 2),
            MusicianOrchestra(3, 1),
            MusicianOrchestra(3, 2),
            MusicianOrchestra(4, 3),
            MusicianOrchestra(5, 3),
            MusicianOrchestra(5, 1)
        ]

        self.manager = OrchestraManager(
            self.orchestras, 
            self.musicians, 
            self.musician_orchestra_links
        )

    def test_get_musicians_with_last_name_starting_A(self):
        result = self.manager.get_musicians_with_last_name_starting('А')
        expected = [
            (self.musicians[0], self.orchestras[0]),
            (self.musicians[2], self.orchestras[0]),
            (self.musicians[4], self.orchestras[2])
        ]
        self.assertEqual(result, expected)

    def test_get_orchestra_min_experience_sorted(self):
        result = self.manager.get_orchestra_min_experience_sorted()
        expected = [
            ('Джазовый Оркестр', 2),
            ('Камерный Оркестр', 3),
            ('Симфонический Оркестр', 5)
        ]
        self.assertEqual(result, expected)

    def test_get_sorted_musician_orchestra_relationships(self):
        result = self.manager.get_sorted_musician_orchestra_relationships()
        expected = [
            ('Александров', 'Симфонический Оркестр'),
            ('Андреев', 'Джазовый Оркестр'),
            ('Андреев', 'Симфонический Оркестр'),
            ('Антонов', 'Симфонический Оркестр'),
            ('Антонов', 'Камерный Оркестр'),
            ('Борисов', 'Джазовый Оркестр'),
            ('Иванов', 'Камерный Оркестр')
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
