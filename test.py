import subprocess,os


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

os.chdir(path+"\mpeg7fex_win32_v2")

os.system("MPEG7Fex.exe CSD 64 imgtest.txt CSD1.txt")