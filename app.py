
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("lr.pkl","rb"))

@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route("/predict.html", methods=['GET','POST'])
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        low = float(request.form["low"])
        high = float(request.form['high'])
        volume = float(request.form['volume'])
        open = float(request.form['open'])
        company = eval(request.form['company'])
        year = int(request.form["year"])
        month = int(request.form['month'])
        day = int(request.form['day'])
        prediction = model.predict([[open, high, low, volume, year, month, day, company]])
        output = prediction[0]
        return render_template("predict.html", prediction="Forecasted closing price on {}/{}/{} is $ {}".format(day, month, year, output))
    else:
        return render_template("predict.html")


if __name__ == '__main__':
    app.run(debug=False)