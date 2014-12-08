import json

#using static paths at the moment, will become dynamic in future commits
json_data_path = ""
json_files =[
            "file1",
            "file2",
            "etc"
            ]

for file in json_files:
        
    json_data = open(json_data_path + file + "_pruned.json", 'r')
        
    data2 = json.load(json_data)
        
    json_data.close()
        
    original_post = data2[0]
    print(original_post)
        
    all_reply_threads = data2[1]["data"]["children"]
