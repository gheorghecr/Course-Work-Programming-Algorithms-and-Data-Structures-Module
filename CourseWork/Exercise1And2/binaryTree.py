"""1) Build a Binary Search Tree (BST) to hold English language words in its nodes. Use a paragraph of
any text in order to extract words and to determine their frequencies.
Input: You should read the paragraph from a suitable file format, such as .txt. The following
tree operations should be implemented: a) Printing the tree in pre-order. b) Finding a word.
Regardless whether found or not found your program should output the path traversed in
determining the answer, followed by yes if found or no, respectively."""

"""2) Implement a function that deletes a node in a binary search tree in a language of your choice"""

def open_read_file(fileName):
    """function to read from a file"""
    try:
        f = open ( fileName , "r")
        words = f.read().rstrip("\n").split(" ")  #rstrip gets rid of \n
        f.close()
        return words
    except (IOError, OSError):
        print ("Error: File not found.")



class BinaryTree():

    def __init__(self, value):
        """initiates the tree"""
        self.value=value
        self.left=None
        self.right=None

    def insert_value(self,value):
        """Exercise 1
        This function will insert the value in the tree

        Title: Trees (Not That Kind!)
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk
        """
        if (self.value == None):
            self.value = BinaryTree(value)
        if (value < self.value):
            if (self.left == None):
                self.left = BinaryTree(value)    # create the node if is not there
            else:
                self.left.insert_value(value)
        else:
            if(self.right == None):
                self.right = BinaryTree(value)   # create the node if is not there
            else:
                self.right.insert_value(value)


    def print_pre_order(self):
        """ Exercise 1 A
        Will print the tree in pree order
        (visits the rots then goes to the childrens from the left side first)

        To complete the exercise I based my self on:
        Title: Trees (Not That Kind!)
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk
        """
        print(self.value)
        if (self.left != None):
            self.left.print_pre_order()
        if (self.right != None):
            self.right.print_pre_order()

    def find_word(self, word_to_find, path = []):
        """Exercise 1 B
        given a a word, will search for it in the binary tree
        return True if word is in the tree and False if not in the Tree,
        will also return the path traversed

        To complete the exercise I based my self on:
        Title: Trees (Not That Kind!)
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk

            Title: Data-Structures-using-Python/BinarySearchTree
            Author: OmkarPathak
            Date: 2017
            Availability: https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/BinarySearchTree.py
        """
        if(self.value == word_to_find):
            path.append(self.value)
            return True, path
        if(self.value > word_to_find):
            # if there is something, (true) same as != None
            if(self.left != None):
                path.append(self.value)
                return self.left.find_word(word_to_find, path)
            else:
                return False, path
        elif(self.value < word_to_find):
            # if there is something, (true), same as != None
            if(self.right != None):
                path.append(self.value)
                return self.right.find_word(word_to_find,path)
            else:
                path.append(self.value)
                return False, path

    def find_min_value(self,value):
        """ this will find the last left children from node

            To complete the exercise I based my self on:
            Title: Data-Structures-using-Python/BinarySearchTree
            Author: OmkarPathak
            Date: 2017
            Availability: https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/BinarySearchTree.py
        """
        min_value = value
        while(min_value.left != None):
            min_value = min_value.left
        return min_value



    def delete_node(self,value_to_delete):
        """Exercise 2
        Given a value to delete this function will delete it from the tree
        and reorganize the tree as necessary

        To complete the exercise I based my self on:
        Title: Trees (Not That Kind!)
            Author: Hintea, D.
            Date: 2018
            Availability: http://moodle.coventry.ac.uk

        Title: Data-Structures-using-Python/BinarySearchTree
            Author: OmkarPathak
            Date: 2017
            Availability: https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/BinarySearchTree.py

        Title: Implementation of binary search tree
            Author: paul kofi osei
            Date: 2018
            Availability: https://codereview.stackexchange.com/questions/191031/implementation-of-binary-search-tree
        """
        if(self.value is None):
            return None
        # goes to the left side if value is smaller then root
        if value_to_delete < self.value:
            self.left = self.left.delete_node(value_to_delete)
        # goes to the right side if value is smaller then root
        elif value_to_delete > self.value:
            self.right = self.right.delete_node(value_to_delete)
        else:
            # if value_to_delete is the same as self.value then This is
            # the  one who need to be deleted
            #  when node has only one child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # deleting when node has 2 childrens
            # first find the inorder successor
            temp = self.find_min_value(self.right) #get the smalest left children from the right children
            self.value = temp.value  ## put at the root
            self.right = self.right.delete_node(temp.value)

        return self


def read_file_start_tree():
    """This will call the function to read from the file and then will
    start the tree by inserting the values and prints it in pre order"""
    fileName = "text.txt"
    words = open_read_file(fileName)
    t = BinaryTree(words[0])
    word_frequencie = {} # dictionary to store the word frequencies
    for word in words:
        x,path = t.find_word(word, path = [])
        #if word already in the tree will not add again and increment the
        #frequencies in the dictionary
        if(x==True):
            if word not in word_frequencie:
                word_frequencie[word] = 1
            else:
                word_frequencie[word] += 1
            continue
        else:
            if word not in word_frequencie:
                word_frequencie[word] = 1
            else:
                word_frequencie[word] += 1
            t.insert_value(word) # since the word isn't in the dictionary will add it
    print("Printing in pre order: ")
    t.print_pre_order()
    print("Word frequencies is: ")
    print(word_frequencie)
    return t

def find_word(t):
    """call the function to check if the word is in the tree and shows the path,
    and then prints yes or no if the word was found or not respectively"""

    word_loking_for = str(input("insert the work that you looking for "))
    x, path  = t.find_word(word_loking_for, path = [])
    if(x==True):
        print("Yes")
    else:
        print("No")
    print("Path is: ")
    print(path)

def delete_word(t):
    """calls the function to delete the one word from the tree, checks first if
    the word exists"""

    word_to_delete= str(input("insert the work that you want to delete "))
    result, path = t.find_word(word_to_delete, path = [])
    if(result==True): # if exists delete it
        t.delete_node(word_to_delete)
        print("Word '" + word_to_delete+ "' deleted sucessufly")
        t.print_pre_order()
    elif(result == False):
        print("Word not in the tree")


if __name__ == '__main__':
    t = read_file_start_tree()
    find_word(t)
    delete_word(t)
