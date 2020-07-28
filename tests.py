import unittest
from main import get_number_from_index, get_empty_list,get_index_from_number

class Test_2048(unittest.TestCase):

#1
    def test_get_number_from_index_1(self):
        self.assertEqual(get_number_from_index(1,2),7)
#2
    def test_get_number_from_index_2(self):
        self.assertEqual(get_number_from_index(3,3),16)
#3
    def test_get_empty_list_1(self):
        a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)
#4
    def test_get_empty_list_2(self):
        a=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)
#5
    def test_get_empty_list_3(self):
        a=[]
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)
#6
    def test_get_index_from_number_1(self):
        self.assertEqual(get_index_from_number(7),(1,2))
#7
    def test_get_index_from_number_2(self):
        self.assertEqual(get_index_from_number(16),(3,3))
#8
    def test_get_index_from_number_3(self):
        self.assertEqual(get_index_from_number(1),(0,0))

    #на случай если вы открываете это приложение не через pyCharm, а другую IDE
    if __name__=='main':
        unittest.main()
