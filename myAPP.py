# NEW
#=====================================
# 1. ADD 2 pages (a.k.a. app.routes)
#    http://127.0.0.1:5000/home
#    http://127.0.0.1:5000/aboutme
# 2. New pages should return ordinary STINGS (No HTML yet)
#=====================================

# To run this program, you have to use FLASK
# Option 1: Name the file app.py or wsgi.py
# flask run

# Option 2: Name the file anyting you want and type (do NOT include the .py file extension)
# flask --app filename run

# Option 3: Run the app in DEBUG mode
# flask --app filename run --debug

# Option 4: Add the following to the bottom of the program and then type python3 filename.py in
#           the terminal to run the website
# if __name__=='__main__':
#     app.run(debug=True)


# 1.  Import the Flask library. This is a web framework (aka web server)
from flask import Flask

# 2. Create a instance of the Flask() class with the only parameter being
#    a "system" variable called __name__. If you want to see what is in __main__
#    create a new Python program file and print it and see what it prints.
#    Call the instance/object "app"
app = Flask(__name__)

# 3. We then use the route() decorator (aka function) to tell Flask what URL should trigger our function.
#    / means the root or "top" level
@app.route("/")     # Default page when you only type the Server URL
@app.route("/home") # Explicit name when you type the Server URL and the route name
# 4. Now let’s tell the website what we should send to the person's web browser who visited our page
def hello_world():
    return "This is the Home Page" # Is this enough to make the webpage work?

# 5. Create another route (aka page)
@app.route("/aboutme")
def secondPage(): # Each route needs it's own FUNCTION
    # Each route needs to return something
    return "This is the About Me page!"

if __name__=='__main__':
    #app.run()
    app.run(debug=True)