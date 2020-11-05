from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html')
    elif request.method =="POST":
        return render_template('home.html', selection=request.form['rad'])

@app.route('/display', methods=['GET', 'POST'])
def display():
    return render_template('display.html', selection=request.form['rad'])

if __name__ == '__main__':
    app.run()