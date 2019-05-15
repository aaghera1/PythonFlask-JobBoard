from flask import flask, render_template

app = Flask(_name_)

@app.route('/')
@app.route('/Jobs')
def jobs():
    return render_template('index.html')
