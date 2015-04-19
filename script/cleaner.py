""" File 'cleaner.py' 
    desc        : cleaning raw data from unrelated stuffs
    how to run  : #python crawl.py [raw_data_input.txt] [cleaned_output.txt]
    (example)   : #python crawl.py data_raw_jkt.txt data_cleaned_jkt.txt
"""
# IMPORT
import re
import datetime
import nltk

# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    file_input = sys.argv[1]
    file_output = sys.argv[2]

# Load stopwords
def load_stopwords():
    stopwords = []
    f = open("stopwords.txt")
    for line in f.readlines():
        stopwords.append(line.replace('\n', '').replace('\r', ''))
    f.close()
    return stopwords

# Filter message
def filter_msg(msg):
    # remove stopwords
    msg = [i for i in msg.split() if i not in stopwords]
    return ' '.join(msg)

# Clean raw_data.txt, remove hashtags, smiley, multiple spaces, links
# Rewrite to data_cleaned.txt
stopwords = load_stopwords()
f_raw = open(file_input, 'r')
f_cleaned = open(file_output, 'w')
for line in f_raw.readlines():
    cap_array = line.split('|')
    cap_id = cap_array[0]
    cap_time = datetime.datetime.fromtimestamp(int(cap_array[1])).strftime('%Y-%m-%d')
    cap_user = cap_array[2] 
    usr_id = cap_array[3]
    usr_follower = cap_array[4]
    usr_post = cap_array[5] 
    cap_text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cap_array[6]).lower() # Removing hashtags
    cap_text = ''.join([i for i in cap_text if not i.isdigit()]) # Removing numbers
    cap_text = filter_msg(cap_text) # Removing stopwords
    cap_text = re.sub(' +',' ',cap_text) # Removing multiple spaces
    f_cleaned.write(cap_id + '|' + cap_time + '|' + cap_user + '|' + usr_id + '|' + usr_follower + '|' + usr_post + '|' + cap_text + '\n')
f_cleaned.close()
f_raw.close()
print "Processing completed"