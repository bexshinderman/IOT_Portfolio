

from flask import Flask, request, render_template
app = Flask(__name__,static_url_path='')


@app.route('/load_data')
def load_data():
    return 'Success'



@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/inspo')
def inspo():
    
    return render_template("inspiration.html")
    
@app.route('/sprint1')
def sprint1():
    
    return render_template("sprint1.html")

@app.route('/sprint2')
def sprint2():
    
    return render_template("sprint2.html")
    
@app.route('/page/<string:title>')
def page(title):
    return 'Title: ' + title
   


@app.route('/form')
def form():
    return render_template("form.html")
@app.route('/response', methods=['POST'])
def response():
    name = request.form.get("name")
    titletag = request.args.get('url')
    return render_template("form.html", name=name)




if __name__ =="__main__":
    app.run(debug=True,port=8080)

