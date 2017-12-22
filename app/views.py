from app import app
from flask import redirect, jsonify
from flask.templating import render_template
import json,main
from flask.globals import request
@app.route("/")
def index():
    #form = submitForm.subForm()
    return render_template("index.html")
@app.route("/baidu")
def baidu():
    return redirect("https://www.baidu.com/")

@app.route("/json",methods =["GET","POST"])
def getjson():
    f = open("app/templates/data.json") 
    data = json.load(f)
    # data = {"nodes":[{"name":"1","value":20,"symbolSize": 60,"category": 0},{"name":"2","value":20,"symbolSize": 60,"category": 1}],"links":[{"source" : '1',"target" : '2'}]}
    #print data
    return jsonify(data) 

@app.route("/get_data",methods =["GET","POST"])
def submit():
    if request.method == 'POST':
        # topic = request.get_json()["search"]
        #main.getdata(topic)
        a = request.get_data()
        data= json.loads(a)
        topic = data["topic"]
        result = main.getdata(topic)
        #print data
        return jsonify(result)  
        
        
    
    return render_template("index.html")