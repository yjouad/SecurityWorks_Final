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
class LargestWords():

    def __init__(self):

        self.largest_words_list = []
        self.words_list = []

    def all_words_list(self, filename):
        """This function will return all the words in the file as a list"""

        try:
            with open(filename, 'r') as infile:
                self.words_list = infile.read().split()
        except ValueError:
            print("File is empty ")
            print("++++++++++++++++++++++++++++++++++++")
            print("+ PLEASE CHECK FILE CONTAINS WORDS +")
            print("++++++++++++++++++++++++++++++++++++")
        except FileNotFoundError:
            print("File does not exist")
            print("+++++++++++++++++++++++++++++++++++++++")
            print("+ PLEASE CHECK FILE LOCATION AND NAME +")
            print("+++++++++++++++++++++++++++++++++++++++")
        return self.words_list

    def all_largest_words_list(self):
        """This function will return all the largest words found"""

        if self.words_list == []:
            print("File is empty ")
            print("++++++++++++++++++++++++++++++++++++")
            print("+ PLEASE CHECK FILE CONTAINS WORDS +")
            print("++++++++++++++++++++++++++++++++++++")

        max_len = len(max(self.words_list, key=len))
        self.largest_words_list = [word for word in self.words_list if len(word) == max_len]
        return self.largest_words_list



