Linked list data structure is used to append, and to keep track of the previous item on the blockchain.

The program was tested on three test cases. In each test case, we can see that with more data being added to the blockchain, each blocks point to the previous blocks, and the first block added to the list does not point to any previous data (as there is None). Here, 'n' is the input size.


Time Complexity - O(1)
The main elementary operation in this program is adding a new block and having it point to the previous block. This is done by appending the new block. Appending takes O(1) time.

Space Complexity - O(n)
Retrieving the last block takes O(1) time as it was last in (first out), and the first one is O(n). Outputting the whole blockchain takes O(n) space.
