from flaskimport flask,render_template,request
imort pickle
app=flask(_name_)
@app.route('/')
def home():
       return render_template('home.html')
 @app.route('/predict')
 def index():
    return render_template("index.html")
    @app.route('/data_predict',method=['post'])
 def predict():
    model=pickle.load(open('liver_analysis.pkl','rb')) 
  prediction=model.predict(data)[0]
 if(prediction ==1):
    return render_template('nochange.html',prediction='You have a liver disease')
else:
    return render_template('chance.html', prediction='you dont have a liver disease')    

if_name_ == '_main_':
    app.run()