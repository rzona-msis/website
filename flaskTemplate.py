# To run this program, you have to use FLASK
# Option 1: Name the file app.py or wsgi.py
# flask run

# Option 2: Name the file anyting you want and type (do NOT include the .py file extension)
# flask --app filename run

# Option 3: Run the app in DEBUG mode
# flask --app filename run --debug

# Option 4: Add the following to the bottom of the program and then type python filename.py in
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


# Write your webpages here ...






# Write code to allow us to type python flaskTemplate.py
if __name__=='__main__':
    #app.run()
    app.run(debug=True)