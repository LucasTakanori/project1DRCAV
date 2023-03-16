import subprocess
import os
import os

dbimglist = "db_img_list.txt"
mpegpth = "\mpeg7fex_win32_v2"
db = "\DATABASE"
outputDescriptorDb = "CSDDB.txt"
outputDescriptorQry = "CSDqry.txt"
featureType = "CSD"
featureParameters = 64
querypth = "\QUERY"
qrylist = "query_list.txt"
def find_images(folder_path, output_file):
    with open(output_file, "w") as f:
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                    f.write(os.path.join(dirpath, filename) + "\n")


def calculate_Descriptor(path, pathScript, pathFiles, featureType, featureParameters, imglist, outputDescriptor):

    find_images(path+pathFiles, path+pathScript + "\\" + imglist)

    os.chdir(path+pathScript)

    os.system("MPEG7Fex.exe " + featureType + " " +
              str(featureParameters) + " " + imglist + " " + outputDescriptor)
    os.chdir(path)


path = os.getcwd()
calculate_Descriptor(path, mpegpth, db, featureType,
                     featureParameters, dbimglist, outputDescriptorDb)

calculate_Descriptor(path, mpegpth, querypth, featureType,
                     featureParameters, qrylist, outputDescriptorQry)

