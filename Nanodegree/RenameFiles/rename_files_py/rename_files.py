import os

def rename_files():
    #1 get file names
    file_list = os.listdir("/Users/SilverMaiden/Downloads/prank")
    print file_list
    #2 rename each filename
    saved_path = os.getcwd()
    os.chdir("/Users/SilverMaiden/Downloads/prank")
    for file_name in file_list:
        os.renames(file_name, file_name.translate(None, "0123456789"))
    print file_list
    os.chdir(saved_path)


rename_files()