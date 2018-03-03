from flask import Flask,render_template
from data import Articles
app=Flask(__name__)
Dummy=Articles()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articlelist():
    return render_template('articles.html',dummy = Dummy)
if __name__ == '__main__':
    app.run(debug=True)
