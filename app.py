from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def form():
    if request.method=='POST':
        distance=request.form.get('distanceInput')
        fuel=request.form.get("fuelConsumed")
        type=request.form.get('fuelInput')
        print(type,distance,fuel)
        if type=='petrol':
            emissions= (float(fuel)*2640)/(float(distance))
        elif type=='diesel':
            emissions=(float(fuel)*2392)/float(distance)
        print(emissions)
        try:
            return f'The carbon emission is {emissions} g CO2/km'
        except:
            return 'Cannot take in values'
    return render_template('form.html')


# @app.route('/result',methods=['POST','GET'])
# def result():
#     if request.method=='POST':
#         result=request.form
#         return render_template('result.html',result=result)

    
if __name__=='__main__':
    app.run(debug=True)
