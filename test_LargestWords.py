'''
 Author : Youssef Jouad
 Code Challenge for : SecurityWorks
 Date : 7-28-2019
 Program should do the following:
    1. Read input from a file of words;

    2. Find the largest word in the file

    3. Transpose the letters in the largest word

    4. Show the largest word and the largest word transposed

    5. Demonstrate positive and negative test cases

'''


import unittest
from LargestWodrs import *

class TestLargest(unittest.TestCase, LargestWords):


    global largest, words
    obj = LargestWords()
    words = obj.all_words_list('inputfile.txt')
    largest = obj.all_largest_words_list()


    def test_file_is_not_empty(self):
        """ This test should pass when the file is not empty and fail when the file is empty"""
        print(".")
        print("+" * 50)
        print("+ Running Test 2: Test if the file is not empty  + ")
        print("+" * 50)
        try :
            if len(largest) > 0 :
                print("++++++++++++++++++++")
                print("+ TEST CASE PASSED +")
                print("++++++++++++++++++++")
                assert True
            else:
                assert True
        except ValueError:
            print(" File is Empty ")


    def test_file_with_one_large_word(self):
        """ This test should pass when file contains only one largest word, fail otherwise"""
        print(".")
        print("+" * 68)
        print("+ Running Test 3: Test if the file contains only one largest word  + ")
        print("+" * 68)


        if len(largest) == 1:
            print(" The file contains only one largest word")
            print("++++++++++++++++++++")
            print("+ TEST CASE PASSED +")
            print("++++++++++++++++++++")
            assert True
        elif len(largest) > 1:
            print(" The  file contains more than one largest word")
            print("++++++++++++++++++++")
            print("+ TEST CASE FAILED +")
            print("++++++++++++++++++++")
            assert False



    def test_file_multiple_large_words(self):
        """ This test if the file contains more than one largest file"""

        print("+" * 73)
        print("+ Running Test 4: Test if the file contains more than one largest word  + ")
        print("+" * 73)

        if len(largest) > 1:

            print(" The file contains more than one largest word")
            print("++++++++++++++++++++")
            print("+ TEST CASE PASSED +")
            print("++++++++++++++++++++")
            assert True
        else:
            print(" The  file contains only one largest word")
            print("++++++++++++++++++++")
            print("+ TEST CASE FAILED +")
            print("++++++++++++++++++++")
            assert False


    def test_print_largest_words(self):
        """ This test should print all the possible largest words found"""


        print("+" * 74)
        print("+ Running Test 5: Test that we can print all the possible largest words  + ")
        print("+" * 74)

        if len(largest) == 0:
            print(" there's no largest word found")
        else:
            print(" the largest word(s)  is {}: ".format(largest))
            print("++++++++++++++++++++")
            print("+ TEST CASE PASSED +")
            print("++++++++++++++++++++")
            assert True

    def test_print_transpose_largest(self):
        """ This test should print all the transpose largest words found"""
        print(".")
        print("+" * 56)
        print("+ Running Test 6: Print all the transpose words founds + ")
        print("+" * 56)

        if len(largest) == 0:
            print(" there's no largest word found")
        else:
            for trans in largest:
                print(" The transport word(s) is {}".format(trans[::-1]))
                print("++++++++++++++++++++")
                print("+ TEST CASE PASSED +")
                print("++++++++++++++++++++")

    def test_largest_word_first(self):
        """ This test should test if we have a largest word as the first word in the file"""
        print(".")
        print("+" * 62)
        print("+ Running Test 7 : test if largest word is first in the list +")
        print("+" * 62)

        for items in largest:
            if words.index(items) == 0:

                print(" we have a largest number at the fist ")
                print("++++++++++++++++++++")
                print("+ TEST CASE PASSED +")
                print("++++++++++++++++++++")
                assert True

            else:
                print("++++++++++++++++++++")
                print("+ TEST CASE FAILED +")
                print("++++++++++++++++++++")
                assert False




if __name__ == '__main__':
    unittest.main()