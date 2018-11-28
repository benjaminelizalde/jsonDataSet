from flask import Flask, url_for, render_template, request, Markup
import os
import json

app = Flask(__name__)

with open('health.json') as health_data:
    diseases = json.load(health_data)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    if "States" not in request.args:
        return render_template('page1.html', disease = disease_lifetime())
    else:
        return render_template('page1.html', disease = disease_lifetime(), start = start(request.args["disease"]) )

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
  
@app.route("/p3")
def render_page3():
    return render_template('page3.html')
    
    
    
    
def disease_lifetime():
    listOfDiseases = []
     for x in diseases:
        if not x["disease"] in listOfDiseases:
            listOfDiseases.append(x["disease"])
     start = ""
     for x in listOfDiseases:
        start = start +  Markup("<option value=\"" + x + "\">" + x + "</option>")
     return start 
    

    
def     first = counties[0]["Age"]["Percent Under 18 Years"]
    for county in counties:
        if county["Age"]["Percent Under 18 Years"] < first:
            first = county["Age"]["Percent Under 18 Years"]
    return first
    
 
if __name__=="__main__":
    app.run(debug=True)
