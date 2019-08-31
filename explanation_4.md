In this program, recursion is used to implement finding the element. Each group is traversed through to see if the user is present. If the user is present then the program outputs True, otherwise False.

Tested with 4 test cases.

Time complexity - O(n!)
The elementary operation is recursion and it is performed n! times as a worst case scenario (which is that user is not present).

Space complexity - O(nm)
As recursion is used, the previous recursive call values are stored in a stack, so the space complexity is O(nm). Here m is the space taken and n is the depth of recursion.
