import json
import os

directory_path = '/home/predator/Desktop/project_files/python/finess_ground/web_scraper/'
output_json='/home/predator/Desktop/project_files/python/experimental_ground/projectFile.json'
dict_list = [] # Create an empty list if the file is empty
char = "-"

def get_file_names(directory_path):
    file_names = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            if filename.endswith(".txt"):
                if filename not in file_names:
                    pathToFile = directory_path+filename
                    file_names.append(pathToFile)
    return file_names

source_files = get_file_names(directory_path)

def transfer_data(file_list):
    dict_list=[]
    for file in file_list:
        source_file = file
        with open(source_file,"r+") as file:
            for line in file.readlines():
                sentence = line.replace('\u201c','').rstrip('\n').replace('\u2019',"'").replace('u\2015','').replace('\u2013',',').replace('\"','').replace('\u201d','')
                if char in line:
                    Author='-'+sentence[sentence.index(char) + len(char):]
                    newSentence=sentence[:sentence.index(char) - len(char)]
                    Quote = newSentence.capitalize()
                    sentence_dict={'Quote': Quote,'Author':Author}
                    dict_list.append(sentence_dict)
                else:
                    Quote = sentence
                    Author = ""
                    sentence_dict={'Quote': Quote,'Author':Author}
                    dict_list.append(sentence_dict)

    return dict_list

quotes_dict = transfer_data(source_files)

with open(output_json, 'a+') as f:
        json.dump(quotes_dict, f, indent=4)
       