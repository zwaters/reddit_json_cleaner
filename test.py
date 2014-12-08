import json

json_data_path = "C:/Users/Annette/Desktop/AskHistoriansJSON/"
json_files =[
               'did_any_of_leonardo_da_vincis_research_actually.json',
               'how_were_individual_ss_soldiers_treated_by_the.json',
               'its_year_xxxx_of_your_specialty_a_dead_body_is.json',
               'was_there_intellectual_exchange_between_ancient.json',
               'what_is_fascism.json'
            ]

for file in json_files:
        
    json_data = open(json_data_path + file + "_pruned.json", 'r')
        
    data2 = json.load(json_data)
        
    json_data.close()
        
    original_post = data2[0]
    print(original_post)
        
    all_reply_threads = data2[1]["data"]["children"]