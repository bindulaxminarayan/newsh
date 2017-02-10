import requests
import json

hostname = 'https://hacker-news.firebaseio.com'
top_stories = '/v0/topstories.json'
output = 'hacker_news_data.txt'

response = requests.get(hostname+top_stories)

if(response.ok):
    items = json.loads(response.content)
    data_file = open(output,'w')
    for item in items:
        item_url = "{0}/v0/item/{1}.json".format(hostname,item)
        item_response = requests.get(item_url)
        item_Data = json.loads(item_response.content)
        item_title = item_Data['title'].encode('ascii','ignore')
        data_file.write(item_title+"\n")
    data_file.close()
else:
    response.raise_for_status()
