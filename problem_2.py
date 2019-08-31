"""
File Recursion
"""

import os


def find_files(suffix, path):
    paths = list()
    contents = os.listdir(path)
    for file in contents:
        #path = os.path.join(dir, file)
        if os.path.isfile(os.path.join(path, file)):
            if file.endswith(suffix):
                paths.append(os.path.join(path, file))
        else:
            paths.extend(find_files(suffix, os.path.join(path, file)))
    return paths

#Test Case 1
print("Test Case 1 - ")
print(find_files(".c", "testdir"))
#expected output - ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

#Test Case 2
print("\nTest Case 2 - ")
print(find_files('.c', 'testdir/subdir3'))
#expected output - ['testdir/subdir3/subsubdir1/b.c']

#Test Case 3
print("\nTest Case 3 - ")
print(find_files(".gitkeep", "testdir"))
#expected output - ['testdir/subdir4/.gitkeep', 'testdir/subdir2/.gitkeep']

#Test Case 4
print("\nTest Case 4 - ")
#print(find_files(" ", "testdir"))
if find_files(" ", "testdir") == []:
    print("Empty directory")
#expected output - Empty directory
