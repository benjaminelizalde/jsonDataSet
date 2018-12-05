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
    if "disease" not in request.args:
          
        return render_template('page1.html', disease = disease_lifetime())
    else:
        chosen_disease = request.args["disease"]
        return render_template('page1.html', disease = disease_lifetime(), startlast = str(disease_start(chosen_disease)) +"-"+ str(disease_end(chosen_disease)))

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
    

    
def  disease_start(chosen_disease):   
    first = 3000
    last = 0
    for x in diseases:
        if x["year"] < first and chosen_disease == x["disease"]:
            first = x["year"]
    return first
    
def  disease_end(chosen_disease):   
    last = 0
    for x in diseases:
        if x["year"] > last and chosen_disease == x["disease"]:
            last = x["year"]
    return last
    
 
if __name__=="__main__":
    app.run(debug=True)
