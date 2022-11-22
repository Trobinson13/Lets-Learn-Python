# importing module1 from another folder
import sys

# Adding Folder_2 to the system path
# this is a custom path relative to my personal machines path to file ...
# ... Update your to match your own config
sys.path.insert(0, '/Users/tre.robinson/Documents/Testing/import_module_tutorial/function_dir')

# importing the add and odd_even function
from module1 import odd_even, add

# calling odd_even function
odd_even(5)

# calling add function
print("Addition of two number is :", add(2, 2))