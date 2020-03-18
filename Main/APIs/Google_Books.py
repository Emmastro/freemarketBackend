import json
import requests

api_token = 'AIzaSyAyxqmIKa6KChE5_PDNHz-Pi5b51iS6sgQ'
api_url_base = 'https://www.googleapis.com/books/v1/'

#headers = {'Content-Type': 'application/json',
#           'Authorization': 'glass-timing-229520 {0}'.format(api_token)}

def get_book_details(search):

    api_url = '{base}volumes?q={search}&key={token}'.format(base=api_url_base, search=search, token=api_token)

    response = requests.get(api_url)#, headers=headers)
    if response.status_code == 200:
        #content = json.loads(response.content.decode('utf-8'))
        
        #book_info = content.get('volumeInfo')
        
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
title subtitle author publisher publishedDate description industryIdentifiers pageCount categories
print(get_book_details('PARLONS KIHUNDE').get('items')[0].get('volumeInfo').get())