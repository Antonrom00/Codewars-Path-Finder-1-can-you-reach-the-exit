import unittest

from src.main import path_finder

a = "\n".join([
    ".W.",
    ".W.",
    "..."
])

b = "\n".join([
    ".W..",
    "....",
    ".w..",
    ".w..",
])

c = "\n".join([
    "......",
    "......",
    "......",
    "......",
    "......",
    "......"
])

d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])

f = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W.",
])

g = "\n".join([
    ".WWW..WW.W.........W..W.W....WW..W.......WW..W..W.",
    "....W..WW.W...W.WW....WWW...........WW..W.WW.....W",
    ".....W..W...W.......W..WW..W......W.........W.W..W",
    "W..W..W.W.W..W.W.W...W...W...W.......W....W....W..",
    ".W...W....W.W...WWW.WWW..W....W..W...WW......W...W",
    "W.........W..W.......W..............W....WWW.W....",
    "....W......W...WW........WWW...W.W.WW..W.......W..",
    ".W..W....W............W.W..WWWW.WW..WWW...WW......",
    "......WWW........WW..W...WWW.WW...........WW.W..WW",
    ".WW......W....W...WWW...........W.....W...W....W.W",
    "....WW...........W.........W...W..................",
    ".W..W....W......W...W.W.......WW...W..............",
    "WWW........WW..W...W...WW.W..WW...WW.WWW...W.WWW..",
    "...W...........W..W.W.W..W..W.W.WW..W.W...........",
    "...........WW..W.WW.....W.....W........W.W..W.W...",
    ".W..W.W..................W...W.........WWWW....W..",
    "....W....W........W........W.W...W.W..W.W....WW...",
    ".W.......W......W.......W.....W....W.W.....WW.....",
    "WW.....W...W........W.W........WWWWW....W.W..W.W..",
    "...WWWW........W.WW.........W........W.W.....W.W.W",
    ".W..W..W....W.W........W........W.........W.......",
    "WW..WW......W....W....W.W...........W.....W.......",
    "..W..W...WWW...W.W.........W..W..W...WW.W.......W.",
    "WW.W.......WW..WW.W..W....WW............W....W....",
    "W.W...W.WW..WW.W....WW........WWW....WWW.W....W...",
    ".......W....W.....W.W.W..W.W.........W.....W....W.",
    "..WW...W.........WW....WW......W....W.......W.WWW.",
    "WW.WW..W.W.WW....WW.W..WW......W.W..........W.W...",
    "W..W.........W..W.........W....W......W......W....",
    "....W..WW.W...W.W.W....W.......W.W...W..WW....WW..",
    "......WW.........W....WW....W..W..WWW.W....W..WW..",
    "W.....W.W..WWW.W...WW....W...W.........WW..W....W.",
    "............W...W....W...W........W....WW...W.W...",
    "............W...W.....W...W..W.W....W..WWWW......W",
    "..W..W...W..............W.W...W......W...W.......W",
    "....W.W...W..W..W...W..W....W.W...........W..W.W.W",
    ".............W...W....W....W.....W..W.......W.....",
    "...WW.W..W....W....W........W.WWW..........W....WW",
    "....WW..W................W..W..W.WW.WW..W....WW..W",
    ".....W.W......W..WW...W..WW...W.....W.W.....WW.W..",
    "WW..WW.W....WW....W..W...W...WW....W.WW....W......",
    "W..........W..WWWW..W..WW.WWW..W.....W..W...W...W.",
    "..W................WW..WW.....W.......WW..WW...W..",
    "W..W..W....W...WW.W......WWW.W.WWW.....WW...W..W.W",
    ".W...W.W.WWW...W.......WW........WW...W.W...W...WW",
    "W..W.....W...W...W......W.WW...W..W..........W....",
    "........W...W..WWW.WW.W.WW........W..W....WWW.W..W",
    ".......W.WW..W........W..W....W....W.W..WW........",
    "..W.........WWWW...WW...W.W.W.W.WW..W....W..W.W...",
    ".....W.....W.....W.W.W.....WW...........WWWW...WW.",
])


class Test(unittest.TestCase):
    def test_a(self):
        self.assertEqual(path_finder(a), True)

    def test_b(self):
        self.assertEqual(path_finder(b), True)

    def test_c(self):
        self.assertEqual(path_finder(c), True)

    def test_d(self):
        self.assertEqual(path_finder(d), False)

    def test_f(self):
        self.assertEqual(path_finder(f), True)

    def test_g(self):
        self.assertEqual(path_finder(g), True)


if __name__ == '__main__':
    unittest.main()
