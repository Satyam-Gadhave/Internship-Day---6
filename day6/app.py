from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(f'message form {name} ({email}): {message}')

    return 'Thank you'
@app.errorhandler(404)
def page_not_found(e):
    return 'page not found'

if __name__ == '__main__':
    app.run(debug=True)