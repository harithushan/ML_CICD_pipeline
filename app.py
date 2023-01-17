from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return """CI CD pipeline has been established.
    just modified the file adian 
    so i have reached the level succesfully 
    am so excited
    love you"""


if __name__=="__main__":
    app.run(debug=True)