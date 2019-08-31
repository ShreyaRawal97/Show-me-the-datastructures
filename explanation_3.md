This is a program that takes a string that needs to be encoded, and produce a prefix-free, variable length binary encoding that minimizes the average codeword length.

The program has been tested with 3 test cases.
Here, n is the input size or the number of characters in the string to be encoded.

Time complexity -
freq() function is used to count the occurrence of each character. It runs in O(n) time. Similarly, the sorting function takes O(n) time as well. Encoding takes log(n)xO(n) time. So time complexity to encode is O(n)log(n).

The time complexity to decode is O(n).

Space complexity - O(n)
The space complexity is O(n).
