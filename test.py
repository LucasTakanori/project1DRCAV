import subprocess,os
import os

dbimglist = "db_img_list.txt"
mpegpth="\mpeg7fex_win32_v2"
db="\DATABASE"
outputDescriptor="CSDDB.txt"
featureType = "CSD" 
featureParameters = 64

def find_images(folder_path, output_file):
    with open(output_file, "w") as f:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                    f.write(os.path.join(dirpath, filename) + "\n")


def calculate_Descriptor(path, pathScript, pathFiles, featureType, featureParameters, imglist, outputDescriptor):

    find_images(path+db, path+db+ "\\" + imglist)

    os.chdir(path+pathScript)

    os.system("MPEG7Fex.exe " + featureType + " " + str(featureParameters) + " " + imglist + " " + outputDescriptor)
#os.system("cd DATABASE")




# Example usage
#folder_path = "/path/to/folder"
#output_file = "/path/to/output.txt"
path = os.getcwd()
calculate_Descriptor(path, mpegpth, db, featureType, featureParameters, dbimglist, outputDescriptor)
