from flask import Flask,render_template,redirect,request,url_for
from urllib.request import urlopen
import json

app=Flask(__name__)
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        distance=request.form.get('distanceInput')
        fuel=request.form.get("fuelConsumed")
        type=request.form.get('fuelInput')
        print(type,distance,fuel)
        if type=='petrol':
            emissions= (float(fuel)*2640)/(float(distance))
            emissions=float("{:.2f}".format(emissions))
        elif type=='diesel':
            emissions=(float(fuel)*2392)/float(distance)
            emissions=float("{:.2f}".format(emissions))

        comparison=122.3
        if comparison<emissions:
            keyword='more'
            percentage=(((emissions-comparison)/emissions) * 100)
        elif comparison>emissions:
            keyword='less'
            percentage=abs((((emissions-comparison)/emissions) * 100))
        percentage=float("{:.2f}".format(percentage))
        
        try:
            return render_template('output.html',emissions=emissions,distance=distance,keyword=keyword,percentage=percentage)
        except:
            return 'Cannot take in values'
    return render_template('form.html')


# @app.route('/result',methods=['POST','GET'])
# def result():
#     if request.method=='POST':
#         result=request.form
#         return render_template('result.html',result=result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/output')
def output():
    return render_template('output.html')
    
if __name__=='__main__':
    app.run(debug=False)
