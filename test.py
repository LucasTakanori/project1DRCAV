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

def read_csd_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        data = []
        for line in lines:
            row = line.strip().split()
            data.append([row[0], [int(x) for x in row[1:]]])
        return data



def find_similar_images(database_file, query_file):
    # read the database file into a dictionary
    database = {}
    with open(database_file, 'r') as f:
        for line in f:
            data = line.strip().split()
            name = data[0]
            coeffs = list(map(int, data[1:]))
            database[name] = coeffs
    
    # read the query file and compare each image to the database
    results = {}
    with open(query_file, 'r') as f:
        for line in f:
            data = line.strip().split()
            query_name = data[0]
            query_coeffs = list(map(int, data[1:]))
            # compute the difference between the query image and each image in the database
            diffs = {}
            for name, coeffs in database.items():
                diff = sum([abs(a-b) for a,b in zip(query_coeffs, coeffs)])
                diffs[name] = diff
            # sort the images in the database by difference and retrieve the 10 most similar
            sorted_diffs = sorted(diffs.items(), key=lambda x: x[1])
            results[query_name] = [name for name,diff in sorted_diffs[:10]]
    
    return results


path = os.getcwd()
calculate_Descriptor(path, mpegpth, db, featureType,
                     featureParameters, dbimglist, outputDescriptorDb)

calculate_Descriptor(path, mpegpth, querypth, featureType,
                     featureParameters, qrylist, outputDescriptorQry)

#image_data = read_csd_file(path+mpegpth+'\CSDDB.txt')

results = find_similar_images(path+mpegpth+'\CSDDB.txt',path+mpegpth+'\CSDqry.txt')
print(results)