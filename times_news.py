import requests
import json

host = "https://newsapi.org/v1/articles"
api_key = 

#Options available latest,top
sort_by = "latest"
source = "the-times-of-india"
output = "times_data.txt"

payload = {"source": source, "sortBy": sort_by, "apiKey": api_key}
response = requests.get(host, params = payload)

if(response.ok):
    items = json.loads(response.content)['articles']
    data_file = open(output,'w')
    for item in items:
        data_file.write(item['title'].encode('ascii','ignore'))
    data_file.close    
else:
    response.raise_for_status()



