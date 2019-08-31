"""
Huffman Tree
"""
import sys
import operator

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

def huffman_encoding(data):
    if not data:
        return data, None

    else:
        frequencies = freq(data)
        sortedFrequenciesList = sortFreq(frequencies)
        mappedSortedFrequencies =  list(map(lambda x: Node(x[0], x[1]), sortedFrequenciesList))
        tree = None

        while(len(mappedSortedFrequencies) > 1):
            firstElement = mappedSortedFrequencies.pop(0)
            secondElement = mappedSortedFrequencies.pop(0)
            rootNode = Node(firstElement.value + secondElement.value, firstElement.value + secondElement.value)
            rootNode.left = firstElement
            rootNode.right = secondElement
            insertElementIntoList(rootNode, mappedSortedFrequencies)
            if(len(mappedSortedFrequencies) == 0):
                tree = Tree(rootNode)
        if tree is None and len(mappedSortedFrequencies) == 1:
            firstElement = mappedSortedFrequencies.pop(0)
            tree = Tree(Node(firstElement.value, firstElement.value))
            tree.root.left = Node(firstElement.key, firstElement.value)

        encodedChars = dict()
        encodeTree(tree.root, "", encodedChars)
        encodedString = ""
        for char in data :
            encodedString += encodedChars[char]
        return encodedString , tree
        pass

def insertElementIntoList(node, sortedFrequencies):
    for index, element in enumerate(sortedFrequencies):
        if node.value < element.value:
            sortedFrequencies.insert(index, node)
            break
        elif(index == len(sortedFrequencies) -1):
            sortedFrequencies.append(node)
            break

def encodeTree(root, string, hoffmanEncodes):
    if(root.right is None and root.left is None):
        hoffmanEncodes[root.key] = string
    else:
        if(root.left is not None):
            encodeTree(root.left, string + "0", hoffmanEncodes)
        if(root.right is not None):
            encodeTree(root.right, string + "1", hoffmanEncodes)



def huffman_decoding(data,root):
    if(root is None):
        return data
    def decode(data, root, index, decodedString):
        if(root.left is None and root.right is None):
            decodedString += root.key
            return index, decodedString
        elif data[index] == "0":
            return decode(data, root.left, index + 1, decodedString)
        else:
            return decode(data, root.right, index + 1, decodedString)
    index = 0
    decodedString = ""
    while(index <= len(data) -1):
        index, decodedString = decode(data, root, index, decodedString)
    return decodedString
    pass

def freq(data):
    freqChar = dict()
    for i in data:
        if i in freqChar:
            freqChar[i] += 1
        else:
            freqChar[i] = 1
    return freqChar

def sortFreq(data):
    sortedData = sorted(data.items(), key=operator.itemgetter(1))
    return sortedData

def testCase1():
    print("Test Case 1: ")
    a_great_sentence = "The bird is a word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)


    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

"""
TEST CASE 1 OUTPUT:

The size of the data is: 67

The content of the data is: The bird is a word

The size of the encoded data is: 36

The content of the encoded data is: 01100111100011110010000010101110001010111101111111001101001010

The size of the decoded data is: 67

The content of the decoded data is: The bird is a word
"""

def testCase2():
    print("Test Case 2: ")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    #data not encoded
    if not encoded_data and not tree:
        print("Empty file. No data encoded.")

"""
TEST CASE 2 OUTPUT:
The size of the data is: 49

The content of the data is:

Empty file. No data encoded.
"""

def testCase3():
    print("Test Case 3: ")
    a_great_sentence = "000000000000"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)


    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

"""
TEST CASE 3 OUTPUT:

The size of the data is: 61

The content of the data is: 000000000000

The size of the encoded data is: 24

The content of the encoded data is: 000000000000

The size of the decoded data is: 61

The content of the decoded data is: 000000000000
"""

testCase1()
testCase2()
testCase3()
