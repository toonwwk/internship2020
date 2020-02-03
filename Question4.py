## Q4.1 & 4.2
import flask
import requests
from flask import request, jsonify
from bs4 import BeautifulSoup

companyDict = {}
logoList = []

page = requests.get('https://theinternship.io')
htmlContent = BeautifulSoup(page.content, 'html.parser')
descriptionList = htmlContent.find_all('span', {'class':'list-company'})
imageList = htmlContent.find_all('div', {'class':'logo-box'})

for i in range(len(imageList)):
    image = imageList[i].img['src']
    description = descriptionList[i].text
    companyDict[description] = image


for imagePath in (sorted(companyDict.keys(), key=len)):
    print(companyDict[imagePath])
    
    logoList.append({'logo' : 'https://theinternship.io/' + companyDict[imagePath]})

logoUrlDict = {'companies' : logoList}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/companies', methods=['GET'])

def createApi():
    return jsonify(logoUrlDict)

app.run()
