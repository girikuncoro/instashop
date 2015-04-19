""" File 'crawl.py' 
    desc        : crawling instagram posts
    how to run  : #python crawl.py [hashtag_query] [result_output.txt]
    (example)   : #python crawl.py onlineshopjkt data_raw_jkt.txt
"""
# IMPORT
import json
from instagram.client import InstagramAPI
from urllib import urlopen

# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    query = sys.argv[1]
    file_output = sys.argv[2]

# CONSTANT
# Register and get client_id here http://instagram.com/developer/
client_id = "ff8b092c952a43b18e6fc41e33da8150"
base_url = "https://api.instagram.com/v1"
endpoints = "tags"
url = "{0}/{1}/{2}/media/recent?client_id={3}".format(base_url, endpoints, query, client_id)
count_caption = 0 # Intialize number of crawled captions

json_data = urlopen(url).read()
response = json.loads(json_data)

# Borrowed code from Danny's
# Write Instagram response to data_raw.txt
f = open(file_output, 'a+')
def write_to_txt(data):
    if 'text' in data['caption']:
        f.write(data['caption']['id'] + '|')
        f.write(data['caption']['created_time'] + '|')
        f.write(data['caption']['from']['username'] + '|')
        f.write(data['caption']['from']['id'] + '|')
        f.write(str(data['likes']['count']) + '|')
        f.write(str(data['comments']['count']) + '|')

        text = data['caption']['text'].replace('\n', ' ').replace('\r', ' ').encode('utf-8')
        f.write(text + '\n')

# Fetch next posts batch
def get_next_page(content):
    if 'pagination' in content:
        if 'next_url' in content['pagination']:
            return content['pagination']['next_url']
        else:
            return ''
    else:
        return ''

# MAIN
# Crawl posts from each page
while url != '':
	next_data = urlopen(url).read()
	response = json.loads(next_data)
	for i in range(0, len(response['data'])):
		if response['data'][i]['caption'] is not None:
			write_to_txt(response['data'][i])
			count_caption += 1
	print 'crawled {0} captions from {1}'.format(count_caption, url)
	url = get_next_page(response)
            
f.close()
print "Successfully crawled {0}".format(count_caption)