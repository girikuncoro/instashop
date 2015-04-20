# An Analysis of Unintended Use of Instagram

## Introduction
The repo contains script that analyzes data from Instagram to perform goals as below:<br>
1. Extracting and visualizing online shop hashtags using D3.js<br>
2. Classifying and visualizing hashtags by countries<br>
3. Crawling and cleaning user posts through Instagram API<br>
4. Plotting the products into 9 categories

## Requirement
0. iPython Notebook (http://ipython.org/notebook.html) and/or Python 2.7<br>
1. numpy<br>
2. matplotlib<br>
3. D3.js

## How to
To collect posts in Instagram with specific tags, run ```crawl.py``` followed by query tags you want to search. It will collect posts written to file. Find below example for crawling data using #onlineshopbali tags that is written to "data_raw.txt".
```
# python crawl.py onlineshopbali data_raw.txt
```
To clean the data, run ```cleaner.py```, it will remove unnecessary stuffs like smiley, hashtags, unrelated links, stopwords, etc and generate output file. Specify the input and output filename on the command line as below example.
```
# python cleaner.py data_raw.txt data_cleaned.txt
```
Find the product categories on ```analyses.ipynb```. This is an iPython Notebook file, if you don't have Notebook you can still see from Notebook viewer: http://nbviewer.ipython.org/github/girikuncoro/instashop/blob/master/script/analyses.ipynb

