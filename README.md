# Internship-Day---6
Building a portfolio website with flask


We brgin by importing flask, render_template and request. Flask is the main flask app class, render_template allows to load and return HTML files from the folder, and requests lets you access data send by forms.
We use the app: to create a variable and access our flask app. Flask() call the flask constructor to create the app.__name__ holds the name of the current module.
@ a decorator that tells flask that the function below is linked to the URL, route() sets the URL route.
def is used to define a function so that it can used again, 'return' send back a response to the browser.
@app.route() sets up another route in the app. method=[POST] only accepts POST requests like when a form is submitted.
@app.errorhandler() adds a default route to catch missing files.
