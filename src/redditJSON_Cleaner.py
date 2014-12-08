#!/usr/bin/env python

import json

json_data_path = "C:/Users/Annette/Desktop/AskHistoriansJSON/"
json_files =[
               'did_any_of_leonardo_da_vincis_research_actually.json',
               'how_were_individual_ss_soldiers_treated_by_the.json',
               'its_year_xxxx_of_your_specialty_a_dead_body_is.json',
               'was_there_intellectual_exchange_between_ancient.json',
               'what_is_fascism.json'
            ]

#sorting the replies so that they're relevant and useful for analysis

for file in json_files:
    
    json_data = open(json_data_path + file, 'r')
    
    data = json.load(json_data)
    
    json_data.close()
    
    original_post = data[0]
    print(original_post)
    
    all_reply_threads = data[1]["data"]["children"]
    
    all_reply_scores = []
    relevent_threads = {}
    
    #obtain reply threads relevant to the discussion
    for post in all_reply_threads:
            
        if post["kind"] == 't1':    
            post_score = post["data"]["score"]
            
            all_reply_scores.append(post_score)
        
    i=0
    temp_scores = []
    while (i < 5):
        n = max(all_reply_scores)
        
        temp_scores.append(all_reply_scores.pop(all_reply_scores.index(n)))
        
        i = i + 1
    
    for post in all_reply_threads:
        
        if post["kind"] == 't1':
        
            post_score = post["data"]["score"]
            
            for score in temp_scores:
                if score == post_score:
                    relevent_threads.update(post)
                    
    data[1]["data"]["children"] = relevent_threads
    
    
    
    with open(json_data_path + file + "_pruned.json", 'w+') as outfile:
        #outfile.write("[")
        json.dump(data, outfile)
        #outfile.write("]")
    #save to file for feature extraction 
    json_data.close()
    
    
    #testing for old_file and pruned_file architectural equality

        
        

