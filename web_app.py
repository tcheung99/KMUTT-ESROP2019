# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route("/")
# # def hello():
# #     return "Hello World!"

# def index():
#     return render_template('index.html')

# if __name__== '__main__':
#     app.run()


#app.py
from flask import Flask

app = Flask('__name__', static_url_path='')


@app.route('/')
def home():    
    return app.send_static_file('view/index.html')

if __name__ == '__main__':
    app.run()