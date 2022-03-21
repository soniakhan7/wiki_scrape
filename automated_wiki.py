import json
import requests
import pandas
from bs4 import BeautifulSoup

def get_html(url):
	source = requests.get(url)
	soup = BeautifulSoup(source.content, 'html.parser')

	return soup

def page_title(html):
	wiki_title = html.find('title')
	wiki_title = str(wiki_title.text)

	return wiki_title


def get_tables(html):
	table_html = html.find_all('table', {'class': 'wikitable'})

	return table_html


def get_data_frames(table_html):
	data_frames = []

	for i in table_html:
		data_frames.append(pandas.read_html(str(i)))

	return data_frames


def get_headers(html, table_html, data_frames):
	list_of_table_headers = []
	content_html = html.find('div', {'id': 'mw-content-text'})
	html_headers = content_html.find_all('h3')
	for i in range(len(data_frames)):
		table_header = None
		if html_headers == []:
			if (table_html[i].find('caption')) != None:
				table_header = table_html[i].find('caption').text
			else:
				table_header = 'Sheet' + str(i+1)
		else:
 			table_header = html_headers[i].text
		table_header = table_header[:31]
		list_of_table_headers.append(table_header)
	return list_of_table_headers


def create_xlsx(title, data_frames, list_of_table_headers):
	with pandas.ExcelWriter(title + '.xlsx' , engine = 'xlsxwriter') as writer:
		for i in range(len(data_frames)):
			parsed_data_frame = data_frames[i][0]
			parsed_data_frame.to_excel(writer, sheet_name = list_of_table_headers[i]) 

url = input('Enter wikipedia page: ')
html = get_html(url)
title = page_title(html)
tables = get_tables(html)
df = get_data_frames(tables)
headers = get_headers(html, tables, df)
create_xlsx(title, df, headers)
