The elementary operation in this program is recursion (so that if the path is a directory, it can repeat the process of finding the target file inside the directory). We perform recursion until there are no more sub directories in each branch.
The program is tested against 4 test cases. Here, 'n' is the input size (the number of files in a directory).

Time complexity - O(n)
We have to go through the whole directory to check every folder for the target suffix file. So the time complexity is O(2^n).

Space complexity - O(nm)
Recursion is used the previous recursive values are stored in a stack. So space complexity is O(nm). Here m is the space and n is the depth of recursion tree.
