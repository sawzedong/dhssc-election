import os
import pandas as pd

movekeywords = ["intro_video", "intro_thumbnail"]
expectfiles = 4

def expandfile(): 
    for filename in os.listdir("./candidate-data/temp"):
        if "DS_Store" not in filename:
            for path in os.listdir(f"./candidate-data/temp/{filename}"):
                try:
                    os.rename(f"./candidate-data/temp/{filename}/{path}", f"./candidate-data/temp/{path}")
                except:
                    print(f"FAILED FOR ./candidate-data/temp/{filename}/{path}")

    

def movefile(cat):
    df = pd.read_excel("./candidate-data/datasheets/candidate_data_final.xlsx", sheet_name=(cat+"_candidate_data"), engine="openpyxl")
    list_of_ids = list(df['id'])
    list_of_names = list(df['name'])
    print(list_of_ids)
    
    for i in range(len(list_of_ids)):
        id = list_of_ids[i]
        name = list_of_names[i]
        fullname = id + " " + name
        for filename in os.listdir(f"./candidate-data/temp/{fullname}"):
            for i in movekeywords:
                if i in filename and "DELETE" not in filename.upper():
                    os.rename(f"./candidate-data/temp/{fullname}/{filename}", f"./candidate-data/assets/{fullname}/{filename}")


    print(f"SUCCESSFULLY UPDATED {cat}")

expandfile()
movefile("jh")
movefile("sh")