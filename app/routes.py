from flask import render_template
from app import app
from app import secretspwd
from app import secrets
import requests
import json
#from dotenv import load_dotenv 
@app.route('/')
@app.route('/index')
def index():
    

    EMAIL = secrets()
    TOKEN = secretspwd()
    zurl = 'https://zccgeorgia.zendesk.com/api/v2/tickets.json'
    user = f'{EMAIL}' + '/token'
    pwd = f'{TOKEN}'
    i = 0
    while zurl:
        response = requests.get(zurl, auth=(user, pwd)) 
        if response.status_code != 200:
            return render_template ('error.html', title = 'Zendesk Tickets', tickets=response.status_code )
        else: 
            if(i==0):
                data = response.json()
                               
            else:
                newdata = response.json()
                newdata = newdata['tickets']
                data['tickets'] = data['tickets'] + newdata;
               
        url = response.json()
        i = i + 1
        zurl = url['next_page']
        
    jsontickets = data['tickets']
    
        
    
    return render_template('index.html', title='Zendesk Tickets', tickets=jsontickets)
   
    
    