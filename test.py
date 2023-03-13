import subprocess,os
import os

def find_images(folder_path, output_file):
    with open(output_file, "w") as f:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                    f.write(os.path.join(dirpath, filename) + "\n")



#os.system("cd DATABASE")
path = os.getcwd()
mylist = os.listdir(path+"\DATABASE")
print(path)
str=("\n"+path+"\DATABASE\\").join(mylist)
str=path+"\DATABASE\\"+str
#open text file
imgpath=path+"\mpeg7fex_win32_v2\imgtest.txt"
print(imgpath)
text_file = open(imgpath, "w")
 
#write string to file
text_file.write(str)
 
#close file
text_file.close()


# Example usage
#folder_path = "/path/to/folder"
#output_file = "/path/to/output.txt"
find_images(path, path+"\mpeg7fex_win32_v2"+"\imgtest1.txt")

os.chdir(path+"\mpeg7fex_win32_v2")

os.system("MPEG7Fex.exe CSD 64 imgtest1.txt CSD12.txt")