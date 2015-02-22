# Purpose of program below
"""this program will decode a secret message from picture files by renaming them
which is done by striping away numbers from file names. Windows by default will
sort file names in alphabetical order"""

import os
def rename_files():

    # get file names from folders where serect message pictures are located
    file_list = os.listdir(r".\prank")
    print(file_list)

    current_dir = os.getcwd()
    #print("Current Directory before: "+current_dir)

   # os.chdir(r"C:\Users\Danish\OneDrive\Documents\Documents\Documents\Documents\Python\prank")
    os.chdir(".\prank")
    print("Current Directory after: "+os.getcwd())
     #For each file, rename filename
    for file_name in file_list:
       orig_file_name = file_name
       os.rename(file_name, file_name.translate("0123456789"))
       print("Before:"+orig_file_name+" | After:"+file_name.translate("0123456789"))
    #Switching back to original directory
   # os.chdir(current_dir)

rename_files()
