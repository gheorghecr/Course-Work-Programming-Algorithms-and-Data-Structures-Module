import unittest
import sys
from binaryTree import BinaryTree

#To complete the exercise I based my self on some tutorials and information such as:
"""Title: *args and **kwargs in python explained
    Author: Yasoob
    Date: 2013
    Availability: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

    Title: Python Tutorial: Unit Testing Your Code with the unittest Module
    Author: Corey Schafer
    Date: 2017
    Availability: https://www.youtube.com/watch?v=6tNS--WetLI&t=1986s

    Title: Binary search tree in Python with simple unit tests.
    Author: Chinmaya Patanaik
    Date: 2016
    Availability: http://chinmayakrpatanaik.com/2016/06/01/Binary-Search-Tree-Python/

    Title: unittest — Unit testing framework
    Author: Python Docs
    Date: n.d.
    Availability: https://docs.python.org/2/library/unittest.html

    Title: Working with the Python Super Function
    Author: PythonForBeginners
    Date: 2017
    Availability: https://www.pythonforbeginners.com/super/working-python-super-function

    Title: Document that unittest.TestCase.__init__ is called once per test
    Author: Python Bug Tracker, Claudiu Popa
    Date: 2013
    Availability: https://bugs.python.org/issue19950
"""

class TestBinarySearchTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        #init method is inialized for each time that a test is run
        super(TestBinarySearchTree, self).__init__(*args, **kwargs)
        self.word = "hey"
        self.binaryTree = BinaryTree(self.word)
        self.words = [  "this", "is", "my", "exercise"]

        for word in self.words:
            self.binaryTree.insert_value(word)

    def test_search(self):
        x, path  = self.binaryTree.find_word("this")
        self.assertEqual(x, True)
        x, path  = self.binaryTree.find_word("not")
        self.assertEqual(x, False)

    def test_delete(self):
        self.binaryTree.delete_node("is")
        x, path  = self.binaryTree.find_word("is")
        self.assertFalse(x)

    def test_pre_order(self):
        print("Pre order Print")
        self.binaryTree.print_pre_order()

if __name__ == '__main__':
    unittest.main()
